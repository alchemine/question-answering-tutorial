"""Timer class.

Context and decorator form timer.
"""
# Author: Dongjin Yoon <djyoon0223@gmail.com>

from base_project.common.logging import *


class Timer(contextlib.ContextDecorator):
    """Timer.

    Examples:
        >>> from time import sleep
        >>> from base_project.common.timer import Timer
        >>> with Timer('Code1'):
        ...     sleep(1)
        * Code1| 1.00s (0.02m)
    """
    def __init__(self, name='Elapsed time'):
        self.name = name

    def __enter__(self):
        self.start_time = perf_counter()
        return self

    def __exit__(self, *exc):
        elapsed_time = perf_counter() - self.start_time
        log(f"* {self.name}| {elapsed_time:.2f}s ({elapsed_time/60:.2f}m)")
        return False