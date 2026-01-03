"""Testing a count_qubits method."""

from __future__ import annotations

import multiprocessing

from ql import LoopMode, count_qubits


def test_loop_mode() -> None:
    """Testing a LoopMode (enum) class."""
    assert LoopMode.PROCESS_POOL.value == 1
    assert LoopMode.THREAD_POOL.value == 2


def test_count_qubits() -> None:
    """Testing a count_qubits method."""
    assert count_qubits() == multiprocessing.cpu_count() - 1
