"""Testing a `Quantum` module."""

from __future__ import annotations

from quantum import LoopMode, QuantumLoop


class TestQuantumLoop:
    """Testing a `QuantumLoop` class."""

    @staticmethod
    def control_sample() -> list[int]:
        """Control sample."""
        return [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

    @staticmethod
    def task(item: int) -> int:
        """Test Quantum."""
        return item * item

    def test_process_pool(self) -> None:
        """Testing a `process_pool` method."""
        data = range(10)
        results = QuantumLoop(self.task, data).run()
        control_sample = self.control_sample()
        for num in results:
            assert num in control_sample

    def test_thread_pool(self) -> None:
        """Testing a `thread_pool` method."""
        data = range(10)
        results = QuantumLoop(
            self.task,
            data,
            mode=LoopMode.THREAD_POOL,
        ).run()
        control_sample = self.control_sample()
        for num in results:
            assert num in control_sample
