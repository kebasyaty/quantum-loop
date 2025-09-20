#### Count qubits

```python
from ql import count_qubits


def main() -> None:
    # Counting the number of conceptual qubits of your computer.
    num = count_qubits()
    print(num)  # => 16


if __name__ == "__main__":
    main()
```

#### QuantumLoop - LoopMode.PROCESS_POOL

```python
from ql import QuantumLoop


def task(num: int) -> int | None:
    """Quantum."""
    return num * num if num % 2 == 0 else None


def main() -> None:
    # Separation of the cycle into quantum algorithms for
    # multiprocessing data processing.
    data = range(1, 10)
    results = QuantumLoop(task, data).run()
    print(results)  # => [4, 16, 36, 64]


if __name__ == "__main__":
    main()
```

#### QuantumLoop - LoopMode.THREAD_POOL

```python
from pathlib import Path
from ql import LoopMode, QuantumLoop


def task(path: str) -> str:
    """Quantum."""
    with Path(path).open("r", encoding="utf-8") as f:
        return f.readline().strip()


def main() -> None:
    # Separation of the cycle into quantum algorithms for
    # multiprocessing data processing.
    data = [
      "assets/files/file_1.txt",
      "assets/files/file_2.txt",
      "assets/files/file_3.txt",
    ]
    results = QuantumLoop(
      task,
      data,
      mode=LoopMode.THREAD_POOL,
    ).run()
    print(results)  # => ["Hello World 1", "Hello World 2", "Hello World 3"]


if __name__ == "__main__":
    main()
```
