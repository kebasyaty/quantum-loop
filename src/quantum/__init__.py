"""A set of tools for quantum calculations.

A Qubit in a regular computer is quantum of algorithm that is executed in
one iteration of a cycle in a separate processor thread.

Quantum is a function with an algorithm of task for data processing.

In this case, the Qubit is not a single information,
but it is a concept of the principle of operation of quantum calculations on a regular computer.
"""

from __future__ import annotations

__all__ = (
    "LoopMode",
    "QuantumLoop",
    "count_qubits",
)

from quantum.loop import LoopMode, QuantumLoop, count_qubits
