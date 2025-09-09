```python
from ql import QuantumLoop, count_qubits


def task(item: int) -> int:
    """Quantum."""
    return item * item


def main() -> None:
    # Counting the number of conceptual qubits of your computer.
    num = count_qubits()
    print(num)  # => 16

    # Separation of the cycle into quantum algorithms for
    # multiprocessing data processing.
    data = range(10)
    results = QuantumLoop(task, data).run()
    print(results)  # => [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


if __name__ == "__main__":
    main()
```
