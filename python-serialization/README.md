<div align="center"><img src="https://github.com/ksyv/holbertonschool-web_front_end/blob/main/baniere_holberton.png"></div>

# Python - Serialization

> **Project series:** Python / Higher-level programming
> **Author:** Javier Valenzani
> **Weight:** 1
> **Level:** Novice

---

## 📚 Table of Contents

* [Description](#description)
* [Learning Objectives](#learning-objectives)
* [Resources](#resources)
* [Project Structure](#project-structure)
* [Tasks](#tasks)

  * [0. Basic Serialization](#0-basic-serialization)
  * [1. Pickling Custom Classes](#1-pickling-custom-classes)
  * [2. Converting CSV to JSON](#2-converting-csv-to-json)
  * [3. Serializing and Deserializing with XML](#3-serializing-and-deserializing-with-xml)

---

## 📖 Description

This project is dedicated to the study of **marshaling** and **serialization** — fundamental concepts in computer science that facilitate the **storage**, **transmission**, and **reconstruction** of data. It focuses on real-world applications and helps build a solid foundation for data handling across various mediums.

---

## 🎯 Learning Objectives

By the end of this project, you will be able to:

* Understand the difference between marshaling and serialization.
* Serialize and deserialize data in formats such as JSON, Pickle, and XML.
* Work with custom objects and persist their state.
* Convert between CSV and JSON.
* Handle errors and data integrity during the serialization process.
* Recognize where serialization is used (e.g., APIs, distributed systems, file persistence).

---

## 🔗 Resources

* [Real Python: Serialization](https://realpython.com/python-serialization-pickle-json/)
* [Real Python: JSON Data Handling](https://realpython.com/python-json/)
* [Python `pickle` module](https://docs.python.org/3/library/pickle.html)
* [Corey Schafer: Pickle Tutorial](https://www.youtube.com/watch?v=2Tw39kZIbhs)
* [CSV to JSON in Python](https://realpython.com/python-csv/)
* [ElementTree XML Processing](https://docs.python.org/3/library/xml.etree.elementtree.html)
* [Socket Programming in Python](https://realpython.com/python-sockets/)

---

## 🗂 Project Structure

```
python-serialization/
├── task_00_basic_serialization.py
├── task_01_pickle.py
├── task_02_csv.py
├── task_03_xml.py
└── README.md
```

---

## ✅ Tasks

### 0. Basic Serialization

**File:** `task_00_basic_serialization.py`

* Implement:

  * `serialize_and_save_to_file(data, filename)`
  * `load_and_deserialize(filename)`
* Uses `json` to save and reload dictionaries.

✔️ 100% Passed

---

### 1. Pickling Custom Classes

**File:** `task_01_pickle.py`

* Class: `CustomObject`

  * Attributes: `name`, `age`, `is_student`
  * Methods:

    * `display()` — print object's state
    * `serialize(filename)` — saves object using `pickle`
    * `deserialize(filename)` — loads object using `pickle`

✔️ 100% Passed

---

### 2. Converting CSV to JSON

**File:** `task_02_csv.py`

* Function: `convert_csv_to_json(csv_filename)`
* Converts `.csv` data into a `.json` file.
* Uses `csv.DictReader` and `json.dump()`
* Handles missing files gracefully.

✔️ 100% Passed

---

### 3. Serializing and Deserializing with XML

**File:** `task_03_xml.py`

* Functions:

  * `serialize_to_xml(dictionary, filename)`
  * `deserialize_from_xml(filename)`
* Uses `xml.etree.ElementTree` to write and parse XML files.

✔️ 100% Passed

---

## 📌 Repository

**GitHub Repo:** [holbertonschool-higher\_level\_programming](https://github.com/holbertonschool-higher_level_programming)
**Directory:** `python-serialization`

---

> *This project will strengthen your understanding of how data can be transformed and transferred between different environments. Mastering serialization is key for building robust, distributed, and persistent applications.*

---

Made with ❤️ at [Holberton School](https://www.holbertonschool.com/)

---
