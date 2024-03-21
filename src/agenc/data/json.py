import json
from pathlib import Path

import polars as pl
from typing_extensions import Self, override

from agenc.core import OfflineEnvironment
from agenc.core.environment import NotLoadedError


class JsonDataLoader(OfflineEnvironment):
    path: Path
    data: pl.DataFrame | None = None

    def __init__(self, path: str | Path) -> None:
        self.path = Path(path)

    @override
    def load(self) -> Self:
        with self.path.open() as file:
            json_content = json.load(file)
        self.data = pl.DataFrame(json_content)
        return self

    @override
    def get_data(self) -> pl.DataFrame:
        if self.data is None:
            raise NotLoadedError
        return self.data