"""Loading data from rosbag topics."""

from collections.abc import Sequence
from pathlib import Path
from typing import Self, override

import polars as pl
from rosbags.dataframe import get_dataframe
from rosbags.highlevel import AnyReader
from rosbags.typesys import Stores, get_types_from_msg, get_typestore

from flowcean.core.environment import OfflineEnvironment
from flowcean.core.environment.base import NotLoadedError


class RosbagLoader(OfflineEnvironment):
    """Environment to load data from a rosbag file.

    The RosbagEnvironment is used to load data from a rosbag file. The
    environment is initialized with the path to the rosbag file and a
    dictionary of topics to load.

    Example:
        ```python
        from flowcean.environments.rosbag import RosbagLoader

        environment = RosbagLoader(
            path="example_rosbag",
            topics={
                "/j100_0000/amcl_pose": [
                    "pose.pose.position.x",
                    "pose.pose.position.y",
                ],
                "/j100_0000/odometry": [
                    "pose.pose.position.x",
                    "pose.pose.position.y",
                ],
            },
        )
        environment.load()
        data = environment.get_data()
        print(data)
        ```
    """

    def __init__(
        self,
        path: str | Path,
        topics: dict[str, list[str]],
        msgpaths: list[str] = [],
    ) -> None:
        """Initialize the RosbagEnvironment.

        Args:
            path: Path to the rosbag.
            topics: Dictionary of topics to load (`topic: [keys]`).
            msgpaths: List of paths to additional message definitions.
        """
        self.path = Path(path)
        self.topics = topics
        self.data = None
        self.typestore = get_typestore(Stores.ROS2_HUMBLE)
        add_types = {}
        for pathstr in msgpaths:
            msgpath = Path(pathstr)
            msgdef = msgpath.read_text(encoding="utf-8")
            add_types.update(
                get_types_from_msg(msgdef, guess_msgtype(msgpath))
            )
            print(f"Added message type: {guess_msgtype(msgpath)}")
        self.typestore.register(add_types)

    @override
    def load(self) -> Self:
        with AnyReader(
            [self.path], default_typestore=self.typestore
        ) as reader:
            features = [
                read_timeseries(reader, topic, keys)
                for topic, keys in self.topics.items()
            ]
            self.data = pl.concat(features, how="horizontal")
        return self

    @override
    def get_data(self) -> pl.DataFrame:
        if self.data is None:
            raise NotLoadedError
        return self.data


def read_timeseries(
    reader: AnyReader,
    topic: str,
    keys: Sequence[str],
) -> pl.DataFrame:
    """Read a timeseries from a rosbag topic.

    Args:
        reader: Rosbag reader.
        topic: Topic name.
        keys: Keys to read from the topic.

    Returns:
        Timeseries DataFrame.
    """
    data_pandas = get_dataframe(reader, topic, keys)
    print(data_pandas)
    # print(data_pandas.applymap(rosmsg_to_dict))
    data = pl.from_pandas(
        get_dataframe(reader, topic, keys).reset_index(names="time"),
    )
    nest_into_timeseries = pl.struct(
        [
            pl.col("time"),
            pl.struct(pl.exclude("time")).alias("value"),
        ]
    )
    return data.select(nest_into_timeseries.implode().alias(topic))


def guess_msgtype(path: Path) -> str:
    """Guess message type name from path.

    Args:
        path: Path to the message file.

    Returns:
        The message definition string.
    """
    name = path.relative_to(path.parents[2]).with_suffix("")
    if "msg" not in name.parts:
        name = name.parent / "msg" / name.name
    return str(name)
