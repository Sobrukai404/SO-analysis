# 🧠 SO-analysis

**SO-analysis** is a Python project focused on simulating and analyzing the performance of file I/O and sorting operations. It leverages system metrics (CPU, memory usage) to provide insights into how resource-intensive operations affect overall system performance — useful for Operating Systems studies and benchmarking exercises.

---

## 📁 Project Structure

```

SO-analysis/
├── generator.py       # Generates unique string files and tracks system resource usage
├── quickSort.py       # Reads and sorts the generated strings with performance logging
├── results.txt        # Output of the sorting operation and its performance stats
└── strings/           # Folder containing the generated .txt files (one per string)

````

---

## ⚙️ Scripts Overview

### `generator.py`

- Generates a specified number of **unique random strings** (2–15 lowercase letters).
- Saves each string into a separate `.txt` file in the `strings/` directory.
- Logs system metrics:
  - Execution time
  - Memory before/after
  - CPU usage
- Outputs stats to the terminal.

#### Example usage:

```bash
pip install psutil
python generator.py
````

---

### `quickSort.py`

* Reads all `.txt` files in `strings/`.
* Sorts the strings using a **custom QuickSort**:

  * Primary key: length of the string
  * Secondary key: alphabetical order
* Monitors and records:

  * Peak memory usage
  * Peak and average CPU usage
  * Total execution time
* Writes the sorted list and stats to `results.txt`.

#### Example usage:

```bash
python quickSort.py
```

---

## 📊 Sample Output (`results.txt`)

```
--- Estatísticas ---
Tempo de execução: 1.8723 segundos
Uso de memória: 12.54 MB
Pico de memória RAM: 45.32 MB
Pico de uso de CPU: 84.6%
Média de uso de CPU: 42.3%
```

---

## 🧪 Requirements

* Python 3.x
* [`psutil`](https://pypi.org/project/psutil/)

Install with:

```bash
pip install psutil
```

---

## 💡 Future Improvements

* Add support for other sorting algorithms (e.g. MergeSort, HeapSort).
* Export charts of performance metrics using `matplotlib`.
* Add CLI arguments for string quantity and algorithm selection.
* Implement multithreading for parallel file reads.

---

## 📄 License

MIT License

---

## ✍️ Author

**Sobrukai404**
[github.com/Sobrukai404](https://github.com/Sobrukai404)
