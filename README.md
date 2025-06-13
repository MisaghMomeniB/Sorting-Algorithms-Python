# 🔢 Sorting Algorithms in Python

A curated collection of classic **sorting algorithm implementations** in Python, designed for learning, comparison, and educational use.

---

## 📋 Table of Contents

1. [Overview](#overview)  
2. [Algorithms Implemented](#algorithms-implemented)  
3. [Installation & Setup](#installation--setup)  
4. [Usage & Examples](#usage--examples)  
5. [Performance Comparison](#performance-comparison)  
6. [Code Structure](#code-structure)  
7. [Testing](#testing)  
8. [Contributing](#contributing)  
9. [License](#license)

---

## 💡 Overview

This repository presents a series of **classical sorting algorithms** implemented in plain Python. Each algorithm includes:

- Clean functional or class-based structure  
- Docstrings and inline comments explaining the key steps  
- Example usage and testcase scaffolding  

Great for algorithm study, teaching, or benchmarking.

---

## ✅ Algorithms Implemented

- **Bubble Sort**  
- **Insertion Sort**  
- **Selection Sort**  
- **Merge Sort**  
- **Quick Sort**  
- **Heap Sort**  
- **Counting Sort** (integer arrays)  
- **Radix Sort** (integer arrays)  
- **TimSort**-like built on Python’s built-in `sorted()` (for reference)

---

## ⚙️ Installation & Setup

```bash
git clone https://github.com/MisaghMomeniB/Sorting-Algorithms-Python.git
cd Sorting-Algorithms-Python
python3 --version # Requires Python 3.7+
````

No external dependencies—everything runs with the Python standard library.

---

## 🚀 Usage & Examples

Each algorithm script can be run directly or imported:

```bash
python bubble_sort.py
```

Example of using it in your code:

```python
from merge_sort import merge_sort

arr = [5, 2, 9, 1, 5, 6]
sorted_arr = merge_sort(arr)
print(sorted_arr)  # [1, 2, 5, 5, 6, 9]
```

Compare algorithms in `benchmark.py` with configurable input sizes:

```bash
python benchmark.py --size 10000 --runs 5
```

---

## 📊 Performance Comparison

Benchmarks are provided in `benchmark.py` to measure:

* Time complexity (best/average/worst cases)
* Memory usage
* Behavior with randomized vs. nearly-sorted data

Results output to console and saved as `benchmark_results.csv`.

---

## 📁 Code Structure

```
Sorting-Algorithms-Python/
├── bubble_sort.py
├── insertion_sort.py
├── selection_sort.py
├── merge_sort.py
├── quick_sort.py
├── heap_sort.py
├── counting_sort.py
├── radix_sort.py
├── tim_sort.py
├── benchmark.py          # Compare runtimes
└── README.md
```

Each algorithm implements:

* A function (e.g., `def quick_sort(arr)`)
* Docstrings explaining time/space complexity
* Standalone `__main__` for demo

---

## 🧪 Testing

Basic assertions included in each algorithm’s `__main__`. To run all tests:

```bash
python benchmark.py --test
```

Or add **pytest** later:

```bash
pip install pytest
pytest .
```

---

## 🤝 Contributing

Contributions welcomed! Ideas:

* Add additional sorts (e.g., Shell Sort, Bucket Sort)
* Implement in in-place vs. functional variants
* Enhance performance profiling
* Add visualizations (e.g., Matplotlib animation)

To contribute:

1. Fork the repo
2. Create a feature branch (`feature/...`)
3. Submit a clean Pull Request with descriptive title

---

## 📄 License

Distributed under **MIT License**. See `LICENSE` file for details.
