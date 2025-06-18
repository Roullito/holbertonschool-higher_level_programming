# 📘 Python - Test-Driven Development

![Holberton Logo](https://raw.githubusercontent.com/holbertonschool/Betty/master/betty-style.png)

> **Project badge:** 100% — Completed
>
> **Level:** Amateur
>
> **By:** Guillaume

---

## 📌 Description

This project introduces the methodology and importance of **Test-Driven Development (TDD)** in Python. You will learn how to:

* Write documentation-based tests using `doctest`
* Create unittests using the `unittest` module
* Write robust code that handles various edge cases
* Use docstrings not only to explain but also to validate behavior through test automation

---

## 🎯 Learning Objectives

* Understand the purpose and principles of TDD
* Create interactive tests with `doctest`
* Document code and test from docstrings
* Cover edge cases and write resilient test suites

---

## 📚 Resources

* [doctest official documentation](https://docs.python.org/3/library/doctest.html)
* [Testing through documentation (doctest)](https://realpython.com/python-testing/#doctest-testing-through-documentation)
* [Unit Tests in Python](https://realpython.com/python-testing/#writing-unit-tests)

---

## ✅ Project Requirements

### Python Scripts

* Python 3.8.5
* pycodestyle compliant (2.7.\*)
* Files end with a new line
* First line: `#!/usr/bin/python3`
* All files are executable

### Test Cases

* Located in `tests/` directory
* Use `doctest` for `.txt` test cases
* Use `unittest` for `.py` test scripts
* Documentation for each module and function is required

---

## 📁 Project Directory Structure

```
python-test_driven_development/
├── 0-add_integer.py
├── 2-matrix_divided.py
├── 3-say_my_name.py
├── 4-print_square.py
├── 5-text_indentation.py
├── 6-max_integer.py
├── 100-matrix_mul.py
├── 101-lazy_matrix_mul.py
├── tests/
│   ├── 0-add_integer.txt
│   ├── 2-matrix_divided.txt
│   ├── 3-say_my_name.txt
│   ├── 4-print_square.txt
│   ├── 5-text_indentation.txt
│   ├── 6-max_integer_test.py
│   ├── 100-matrix_mul.txt
│   └── 101-lazy_matrix_mul.txt
└── README.md
```

---

## 📌 Tasks Summary

| File                                               | Task | Description                                   |
| -------------------------------------------------- | ---- | --------------------------------------------- |
| `0-add_integer.py`                                 | 0    | Add two integers with strict type checks      |
| `2-matrix_divided.py`                              | 1    | Divide matrix elements and validate structure |
| `3-say_my_name.py`                                 | 2    | Print formatted name with type checks         |
| `4-print_square.py`                                | 3    | Print a square with # characters              |
| `5-text_indentation.py`                            | 4    | Print text with indentation on `.`, `?`, `:`  |
| `6-max_integer.py` + `tests/6-max_integer_test.py` | 5    | Find max integer using `unittest`             |
| `100-matrix_mul.py`                                | 6    | Matrix multiplication with manual validation  |
| `101-lazy_matrix_mul.py`                           | 7    | Matrix multiplication using NumPy             |

---

## 🧪 Testing Commands

### Doctest:

```bash
$ python3 -m doctest -v ./tests/0-add_integer.txt
```

### Unittest:

```bash
$ python3 -m unittest tests/6-max_integer_test.py
```

---

## 📎 Notes

* Tests must pass for full score.
* Prioritize writing tests *before* implementation.
* Think in edge cases: null inputs, wrong types, empty matrices, etc.

---

## 📬 Contact

Project by Holberton School. For questions, ask your peers or your learning advisor.

---

## 🏁 End

You're now equipped with foundational TDD skills. Continue writing robust, testable code!

