"""Testing a Loop module."""

from __future__ import annotations

from pathlib import Path

from ql import LoopMode, QuantumLoop


def task_1(num: int) -> int | None:
    """Test Quantum.

    (LoopMode.PROCESS_POOL)
    """
    return num * num if num % 2 == 0 else None


def task_2(path: str) -> str:
    """Test Quantum.

    (LoopMode.THREAD_POOL)
    """
    with Path(path).open("r", encoding="utf-8") as f:
        return f.readline().strip()


class TestQuantumLoop:
    """Testing a QuantumLoop class."""

    def test_process_pool(self) -> None:
        """Testing a `process_pool` method."""
        data = range(1, 10)
        results = QuantumLoop(task_1, data).run()
        assert len(results) == 4
        control_sample = [4, 16, 36, 64]
        for num in results:
            assert num in control_sample

    def test_thread_pool(self) -> None:
        """Testing a `thread_pool` method."""
        data = [
            "assets/files/file_1.txt",
            "assets/files/file_2.txt",
            "assets/files/file_3.txt",
        ]
        results = QuantumLoop(
            task_2,
            data,
            mode=LoopMode.THREAD_POOL,
        ).run()
        assert len(results) == 3
        control_sample = ["Hello World 1", "Hello World 2", "Hello World 3"]
        for num in results:
            assert num in control_sample
