"""A set of tools for quantum calculations.

A Qubit in a regular computer is quantum of algorithm that is executed in
one iteration of a cycle in a separate processor thread.

Quantum is a function with an algorithm of task for data processing.

In this case, the Qubit is not a single information,
but it is a concept of the principle of operation of quantum calculations on a regular computer.
"""

from __future__ import annotations

__all__ = (
    "QuantumLoop",
    "LoopMode",
    "count_qubits",
)


from ql.loop import QuantumLoop
from ql.utils import LoopMode, count_qubits
