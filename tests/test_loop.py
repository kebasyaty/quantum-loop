"""Testing a Loop module."""

from __future__ import annotations

from ql import LoopMode, QuantumLoop


def task(num: int) -> int | None:
    """Test Quantum."""
    if num % 2 == 0:
        return num * num
    return None


class TestQuantumLoop:
    """Testing a QuantumLoop class."""

    @staticmethod
    def data():
        """Test Data."""
        return range(1, 10)

    @staticmethod
    def control_sample() -> list[int]:
        """Control sample of results."""
        return [4, 16, 36, 64]

    def test_process_pool(self) -> None:
        """Testing a `process_pool` method."""
        data = self.data()
        results = QuantumLoop(task, data).run()
        assert len(results) == 4
        control_sample = self.control_sample()
        for num in results:
            assert num in control_sample

    def test_thread_pool(self) -> None:
        """Testing a `thread_pool` method."""
        data = self.data()
        results = QuantumLoop(
            task,
            data,
            mode=LoopMode.THREAD_POOL,
        ).run()
        assert len(results) == 4
        control_sample = self.control_sample()
        for num in results:
            assert num in control_sample
