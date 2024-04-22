"""Utilities for commandline usage of experiments.

This module provides common utilities for commandline usage of experiments. It
is intended to be used as a library for writing commandline interfaces for
experiments.
"""

__all__ = [
    "initialize_logging",
    "DEFAULT_RUNTIME_CONFIGURATION_PATH",
]


from .logging import (
    DEFAULT_RUNTIME_CONFIGURATION_PATH,
    initialize_logging,
)
