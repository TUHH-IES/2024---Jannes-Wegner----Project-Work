import logging
from typing import Self

logger = logging.getLogger(__name__)


class RandomState:
    _instance = None
    seed: int

    @classmethod
    def initialize(cls, seed: int) -> None:
        cls._instance = super().__new__(cls)
        cls._instance.seed = seed

    def __new__(cls) -> Self:
        print("RandomState.__new__()")
        if cls._instance is None:
            print("instance is None")
            cls._instance = super().__new__(cls)
            # Put any initialization here.
        print("returning instance")
        return cls._instance
