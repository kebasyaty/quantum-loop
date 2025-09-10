"""Utils.

The module contains the following tools:

- `LoopMode` - Quantum loop mode.
- `count_qubits()` - Counting the number of conceptual qubits of your computer.
"""

from __future__ import annotations

import multiprocessing
from enum import Enum


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
        >>> from ql import count_qubits
        >>> count_qubits()
        16

    Returns:
        The number of conceptual qubits.
    """
    return multiprocessing.cpu_count()
