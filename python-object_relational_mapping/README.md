<div align="center"><img src="https://github.com/ksyv/holbertonschool-web_front_end/blob/main/baniere_holberton.png"></div>

# Python - Object-Relational Mapping

This repository contains scripts and modules that demonstrate how to interface with a MySQL database using Python. It showcases both direct SQL manipulation using `MySQLdb` and high-level database interaction via the `SQLAlchemy` ORM.

## Background Context

The goal of this project is to bridge two powerful domains in software development: **Databases** and **Python**. It is split into two main parts:

1. **Using MySQLdb:** Direct SQL queries are performed through Python.
2. **Using SQLAlchemy:** An Object-Relational Mapper (ORM) is used to manipulate database records through Python objects without writing raw SQL queries.

## Learning Objectives

By completing this project, students will be able to:

* Connect to a MySQL database using Python.
* Perform SQL operations (SELECT, INSERT, UPDATE, DELETE) via Python scripts.
* Understand the concept and advantages of ORM.
* Use SQLAlchemy to abstract database manipulation.
* Define Python classes that map to MySQL tables.
* Avoid SQL injection vulnerabilities using parameterized queries.

## Technologies & Requirements

* Python 3.8.5
* MySQL 8.0
* MySQLdb (mysqlclient) v2.0.x
* SQLAlchemy v1.4.x
* Ubuntu 20.04 LTS

## Installation

```bash
sudo apt update
sudo apt install mysql-server python3-dev libmysqlclient-dev zlib1g-dev
pip3 install mysqlclient SQLAlchemy
```

## Usage

All Python files are executable and should be run using the following format:

```bash
./<script_name.py> <mysql_username> <mysql_password> <database_name> [<optional_argument>]
```

## Project Structure

```bash
.
├── 0-select_states.py               # Selects all states from MySQL using MySQLdb
├── 1-filter_states.py              # Filters states starting with 'N'
├── 2-my_filter_states.py          # Filters states using user input (vulnerable)
├── 3-my_safe_filter_states.py     # Safe version using parameterized queries
├── 4-cities_by_state.py           # Lists cities and their state
├── 5-filter_cities.py             # Filters cities of a specific state
├── model_state.py                 # Defines SQLAlchemy model for State
├── 6-model_state.py               # Creates the states table
├── 7-model_state_fetch_all.py     # Lists all states using SQLAlchemy
├── 8-model_state_fetch_first.py   # Fetches the first state
├── 9-model_state_filter_a.py      # Lists states containing 'a'
├── 10-model_state_my_get.py       # Gets a state by name
├── 11-model_state_insert.py       # Inserts a new state
├── 12-model_state_update_id_2.py  # Updates state with id 2
├── 13-model_state_delete_a.py     # Deletes states containing 'a'
├── model_city.py                  # Defines SQLAlchemy model for City
├── 14-model_city_fetch_by_state.py # Lists all cities with state names
└── README.md
```

## Author

Student at Holberton School

## Acknowledgements

Thanks to the Holberton School curriculum team for designing this comprehensive project to help students build real-world backend skills using Python and SQL.

---

> ✨ "ORMs are like magic for your database. Use them wisely."

