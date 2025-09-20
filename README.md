<div align="center">
  <p align="center">
    <a href="https://github.com/kebasyaty/quantum-loop">
      <img
        height="80"
        alt="Logo"
        src="https://raw.githubusercontent.com/kebasyaty/quantum-loop/main/assets/logo.svg">
    </a>
  </p>
  <p>
    <h1>quantum loop</h1>
    <h3>A set of tools for quantum calculations.</h3>
    <p align="center">
      <a href="https://github.com/kebasyaty/quantum-loop/actions/workflows/test.yml" alt="Build Status"><img src="https://github.com/kebasyaty/quantum-loop/actions/workflows/test.yml/badge.svg" alt="Build Status"></a>
      <a href="https://kebasyaty.github.io/quantum-loop/" alt="Docs"><img src="https://img.shields.io/badge/docs-available-brightgreen.svg" alt="Docs"></a>
      <a href="https://pypi.python.org/pypi/quantum-loop/" alt="PyPI pyversions"><img src="https://img.shields.io/pypi/pyversions/quantum-loop.svg" alt="PyPI pyversions"></a>
      <a href="https://pypi.python.org/pypi/quantum-loop/" alt="PyPI status"><img src="https://img.shields.io/pypi/status/quantum-loop.svg" alt="PyPI status"></a>
      <a href="https://pypi.python.org/pypi/quantum-loop/" alt="PyPI version fury.io"><img src="https://badge.fury.io/py/quantum-loop.svg" alt="PyPI version fury.io"></a>
      <br>
      <a href="https://github.com/kebasyaty/quantum-loop/issues"><img src="https://img.shields.io/github/issues/kebasyaty/quantum-loop.svg" alt="GitHub issues"></a>
      <a href="https://pepy.tech/projects/quantum-loop"><img src="https://static.pepy.tech/badge/quantum-loop" alt="PyPI Downloads"></a>
      <a href="https://github.com/kebasyaty/quantum-loop/blob/main/LICENSE" alt="GitHub license"><img src="https://img.shields.io/github/license/kebasyaty/quantum-loop" alt="GitHub license"></a>
      <a href="https://mypy-lang.org/" alt="Types: Mypy"><img src="https://img.shields.io/badge/types-Mypy-202235.svg?color=0c7ebf" alt="Types: Mypy"></a>
      <a href="https://docs.astral.sh/ruff/" alt="Code style: Ruff"><img src="https://img.shields.io/badge/code%20style-Ruff-FDD835.svg" alt="Code style: Ruff"></a>
      <a href="https://github.com/kebasyaty/quantum-loop" alt="PyPI implementation"><img src="https://img.shields.io/pypi/implementation/quantum-loop" alt="PyPI implementation"></a>
      <br>
      <a href="https://pypi.org/project/quantum-loop"><img src="https://img.shields.io/pypi/format/quantum-loop" alt="Format"></a>
      <a href="https://github.com/kebasyaty/quantum-loop"><img src="https://img.shields.io/github/languages/top/kebasyaty/quantum-loop" alt="Top"></a>
      <a href="https://github.com/kebasyaty/quantum-loop"><img src="https://img.shields.io/github/repo-size/kebasyaty/quantum-loop" alt="Size"></a>
      <a href="https://github.com/kebasyaty/quantum-loop"><img src="https://img.shields.io/github/last-commit/kebasyaty/quantum-loop/main" alt="Last commit"></a>
      <a href="https://github.com/kebasyaty/quantum-loop/releases/" alt="GitHub release"><img src="https://img.shields.io/github/release/kebasyaty/quantum-loop" alt="GitHub release"></a>
    </p>
    <p align="center">
      A Qubit in a regular computer is quantum of algorithm that is executed in
      <br>
      one iteration of a cycle in a separate processor thread.
      <br>
      Quantum is a function with an algorithm of task for data processing.
      <br>
      In this case, the Qubit is not a single information,
      <br>
      but it is a concept of the principle of operation of quantum calculations on a regular computer.
    </p>
  </p>
</div>

##

<br>

## Documentation

Online browsable documentation is available at [https://kebasyaty.github.io/quantum-loop/](https://kebasyaty.github.io/quantum-loop/ "Documentation").

## Requirements

[View the list of requirements](https://github.com/kebasyaty/quantum-loop/blob/v0/REQUIREMENTS.md "Requirements").

## Installation

```shell
uv add quantum-loop
```

## Usage

```python
"""Count qubits."""

from ql import count_qubits


def main() -> None:
    # Counting the number of conceptual qubits of your computer.
    num = count_qubits()
    print(num)  # => 16


if __name__ == "__main__":
    main()
```

```python
"""QuantumLoop - LoopMode.PROCESS_POOL ."""
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

```python
"""QuantumLoop - LoopMode.THREAD_POOL ."""

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

## Changelog

[View the change history](https://github.com/kebasyaty/quantum-loop/blob/v0/CHANGELOG.md "Changelog").

## License

This project is licensed under the [MIT](https://github.com/kebasyaty/quantum-loop/blob/main/LICENSE "MIT").
