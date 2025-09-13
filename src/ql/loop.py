"""A set of tools for quantum calculations.

A Qubit in a regular computer is quantum of algorithm that is executed in
one iteration of a cycle in a separate processor thread.

Quantum is a function with an algorithm of task for data processing.

In this case, the Qubit is not a single information,
but it is a concept of the principle of operation of quantum calculations on a regular computer.

The module contains the following tools:

- `QuantumLoop` - Separation of the cycle into quantum algorithms for multiprocessing data processing.
"""

from __future__ import annotations

import concurrent.futures
from collections.abc import Callable, Iterable
from typing import Any, Never, assert_never

from ql.utils import LoopMode


class QuantumLoop:
    """Separation of the cycle into quantum algorithms for multiprocessing data processing.

    Examples:
        >>> from ql import QuantumLoop
        >>> def task(num: int) -> int | None:
        ... return num * num if num % 2 == 0 else None
        >>> data = range(1, 10)
        >>> QuantumLoop(task, data).run()
        [4, 16, 36, 64]

    Args:
        task: Function with a task algorithm.
        data: The data that needs to be processed.
        max_workers: The maximum number of processes that can be used to
                     execute the given calls. If None or not given then as many
                     worker processes will be created as the machine has processors.
        timeout: The number of seconds to wait for the result if the future isn't done.
                 If None, then there is no limit on the wait time.
        mode: The operating mode for a quantum loop: LoopMode.PROCESS_POOL | LoopMode.THREAD_POOL.
    """

    def __init__(  # noqa: D107
        self,
        task: Callable,
        data: Iterable[Any],
        max_workers: int | None = None,
        timeout: float | None = None,
        mode: LoopMode = LoopMode.PROCESS_POOL,
    ) -> None:
        self.task = task
        self.data = data
        self.max_workers = max_workers
        self.timeout = timeout
        self.mode = mode

    def process_pool(self) -> list[Any]:
        """Better suitable for operations for which large processor resources are required."""
        task = self.task
        data = self.data
        timeout = self.timeout
        results: list[Any] = []
        with concurrent.futures.ProcessPoolExecutor(self.max_workers) as executor:
            for item in data:
                future = executor.submit(task, item)
                result = future.result(timeout)
                if result is not None:
                    results.append(result)
        return results

    def thread_pool(self) -> list[Any]:
        """More suitable for tasks related to input-output
        (for example, network queries, file operations),
        where GIL is freed during input-output operations."""  # noqa: D205, D209
        task = self.task
        data = self.data
        timeout = self.timeout
        results: list[Any] = []
        with concurrent.futures.ThreadPoolExecutor(self.max_workers) as executor:
            for item in data:
                future = executor.submit(task, item)
                result = future.result(timeout)
                if result is not None:
                    results.append(result)
        return results

    def run(self) -> list[Any]:
        """Run the quantum loop."""
        results: list[Any] = []
        match self.mode.value:
            case 1:
                results = self.process_pool()
            case 2:
                results = self.thread_pool()
            case _ as unreachable:
                assert_never(Never(unreachable))
        return results
