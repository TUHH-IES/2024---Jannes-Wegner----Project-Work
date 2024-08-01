import unittest

import polars as pl
from polars.testing import assert_frame_equal

from flowcean.transforms import OneCold


class OneColdTransform(unittest.TestCase):
    def test_single(self) -> None:
        transform = OneCold(["a"])

        data_frame = pl.DataFrame(
            [
                {"a": 1, "b": 2, "c": 3},
                {"a": 4, "b": 5, "c": 6},
                {"a": 7, "b": 8, "c": 9},
                {"a": 10, "b": 11, "c": 12},
            ],
        )
        transformed_data = transform.transform(data_frame)

        assert_frame_equal(
            transformed_data,
            pl.DataFrame(
                {
                    "a_1": [0, 1, 1, 1],
                    "a_4": [1, 0, 1, 1],
                    "a_7": [1, 1, 0, 1],
                    "a_10": [1, 1, 1, 0],
                    "b": [2, 5, 8, 11],
                    "c": [3, 6, 9, 12],
                },
            ),
            check_column_order=False,
        )

    def test_multiple(self) -> None:
        transform = OneCold(["a", "b"])

        data_frame = pl.DataFrame(
            [
                {"a": 1, "b": 2, "c": 3},
                {"a": 4, "b": 5, "c": 6},
                {"a": 7, "b": 8, "c": 9},
                {"a": 10, "b": 11, "c": 12},
            ],
        )
        transformed_data = transform.transform(data_frame)

        assert_frame_equal(
            transformed_data,
            pl.DataFrame(
                {
                    "a_1": [0, 1, 1, 1],
                    "a_4": [1, 0, 1, 1],
                    "a_7": [1, 1, 0, 1],
                    "a_10": [1, 1, 1, 0],
                    "b_2": [0, 1, 1, 1],
                    "b_5": [1, 0, 1, 1],
                    "b_8": [1, 1, 0, 1],
                    "b_11": [1, 1, 1, 0],
                    "c": [3, 6, 9, 12],
                },
            ),
            check_column_order=False,
        )

    def test_non_integer(self) -> None:
        transform = OneCold(["a"])

        data_frame = pl.DataFrame({"a": [1.456, 17.24, 42.0]})
        transformed_data = transform.transform(data_frame)

        assert_frame_equal(
            transformed_data,
            pl.DataFrame({"a": [1.456, 17.24, 42.0]}),
            check_column_order=False,
        )


if __name__ == "__main__":
    unittest.main()
