```python
from ql import QuantumLoop, count_qubits


def task(num: int) -> int | None:
    """Quantum."""
    return num * num if num % 2 == 0 else None


def main() -> None:
    # Counting the number of conceptual qubits of your computer.
    num = count_qubits()
    print(num)  # => 16

    # Separation of the cycle into quantum algorithms for
    # multiprocessing data processing.
    data = range(1, 10)
    results = QuantumLoop(task, data).run()
    print(results)  # => [4, 16, 36, 64]


if __name__ == "__main__":
    main()
```
