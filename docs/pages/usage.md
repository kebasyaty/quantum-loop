```python
from quantum import LoopMode, QuantumLoop, count_qubits

# Counting the number of conceptual qubits of your computer.
num = count_qubits()
print(num)  # => 16

def task(item):
    """Quantum."""
    return item * item

data = range(10)

# Separation of the cycle into quantum algorithms for
# multiprocessing data processing.
results = QuantumLoop(task, data).run()
print(results)  # => [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```
