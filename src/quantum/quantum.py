"""A set of tools for quantum calculations.

A Qubit in a regular computer is quantum of algorithm that is executed in
one iteration of a cycle in a separate processor thread.

Quantum is a function with an algorithm of task for data processing.

In this case, the Qubit is not a single information,
but it is a concept of the principle of operation of quantum calculations on a regular computer.

The module contains the following tools:

- `LoopMode` - Quantum loop mode.
- `count_qubits()` - Counting the number of conceptual qubits of your computer.
- `QuantumLoop` - Separation of the cycle into quantum algorithms for multiprocessing data processing.
"""

from __future__ import annotations

import concurrent.futures
import multiprocessing
from collections.abc import Callable, Iterable
from enum import Enum
from typing import Any, Never, assert_never


class LoopMode(Enum):
    """Quantum loop mode."""

    PROCESS_POOL = 1
    THREAD_POOL = 2


def count_qubits() -> int:
    """Counting the number of conceptual qubits of your computer.

    Conceptual qubit is quantum of algorithm (task) that is executed in
    iterations of a cycle in a separate processor thread.

    Quantum of algorithm is a function for data processing.

    Examples:
        >>> from xloft.quantum import count_qubits
        >>> count_qubits()
        16

    Returns:
        The number of conceptual qubits.
    """
    return multiprocessing.cpu_count()


class QuantumLoop:
    """Separation of the cycle into quantum algorithms for multiprocessing data processing.

    Examples:
        >>> from xloft.quantum import QuantumLoop
        >>> def task(item):
        ... return item * item
        >>> data = range(10)
        >>> QuantumLoop(task, data).run()
        [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

    Args:
        task: Function with a task algorithm.
        data: The data that needs to be processed.
        max_workers: The maximum number of processes that can be used to
                     execute the given calls. If None or not given then as many
                     worker processes will be created as the machine has processors.
        timeout: The maximum number of seconds to wait. If None, then there
                 is no limit on the wait time.
        chunksize: The size of the chunks the iterable will be broken into
                   before being passed to a child process. This argument is only
                   used by ProcessPoolExecutor; it is ignored by ThreadPoolExecutor.
        mode: The operating mode for a quantum loop: LoopMode.PROCESS_POOL | LoopMode.THREAD_POOL.
    """

    def __init__(  # noqa: D107
        self,
        task: Callable,
        data: Iterable[Any],
        max_workers: int | None = None,
        timeout: float | None = None,
        chunksize: int = 1,
        mode: LoopMode = LoopMode.PROCESS_POOL,
    ) -> None:
        self.quantum = task
        self.data = data
        self.max_workers = max_workers
        self.timeout = timeout
        self.chunksize = chunksize
        self.mode = mode

    def process_pool(self) -> list[Any]:
        """Better suitable for operations for which large processor resources are required."""
        with concurrent.futures.ProcessPoolExecutor(self.max_workers) as executor:
            results = list(
                executor.map(
                    self.quantum,
                    self.data,
                    timeout=self.timeout,
                    chunksize=self.chunksize,
                ),
            )
        return results  # noqa: RET504

    def thread_pool(self) -> list[Any]:
        """More suitable for tasks related to input-output
        (for example, network queries, file operations),
        where GIL is freed during input-output operations."""  # noqa: D205, D209
        with concurrent.futures.ThreadPoolExecutor(self.max_workers) as executor:
            results = list(
                executor.map(
                    self.quantum,
                    self.data,
                    timeout=self.timeout,
                    chunksize=self.chunksize,
                ),
            )
        return results  # noqa: RET504

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
