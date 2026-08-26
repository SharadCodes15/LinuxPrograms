# SQLite3 Viewer

A simple SQLite3 database viewer written in Python.

The project provides two interfaces for browsing SQLite databases:

- 🖥️ **CLI Version** — terminal-based SQLite database viewer
- 🌐 **Flask Version** — browser-based SQLite database viewer

Both versions are designed for **viewing and exploring databases without requiring users to write SQL queries**.

## Features

- Open SQLite `.db`, `.sqlite`, and `.sqlite3` files
- Automatically detect database tables
- Browse table records
- View table schema
- Display column names and data types
- No SQL query input required
- Simple and lightweight
- Uses Python's built-in `sqlite3` module

---

# Versions

## 🖥️ CLI Version

The CLI version allows you to inspect an SQLite database directly from the terminal.

### Run

```bash
python cli.py
```

The application will guide you through selecting a database and table.

Example:

```text
SQLite3 Viewer
==============

Select database:
1. example.db
2. users.db
3. shop.sqlite

Enter choice: 1

Tables:
1. users
2. products
3. orders

Enter choice: 1

Users
-----

+----+----------+---------------------+
| id | name     | email               |
+----+----------+---------------------+
| 1  | Alice    | alice@example.com   |
| 2  | Bob      | bob@example.com     |
+----+----------+---------------------+
```

No SQL knowledge is required.

---

# 🌐 Flask Version

The Flask version provides a web interface for browsing SQLite databases.

### Run

```bash
python app.py
```

Then open:

```text
http://127.0.0.1:5000
```

The web interface allows you to:

1. Select a database.
2. View available tables.
3. Select a table.
4. View its schema.
5. Browse its records.

There is **no SQL query editor** in the Flask interface.

---

# Project Structure

```text
sqlite3-viewer/
│
├── cli.py
├── app.py
├── requirements.txt
├── README.md
├── LICENSE
│
├── databases/
│   └── example.db
│
├── templates/
│   ├── index.html
│   ├── tables.html
│   └── table.html
│
└── static/
    ├── css/
    │   └── style.css
    └── js/
        └── app.js
```

---

# Installation

Clone the repository:

```bash
git clone https://github.com/USERNAME/sqlite3-viewer.git
cd sqlite3-viewer
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it.

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

Install Flask:

```bash
pip install -r requirements.txt
```

The CLI version uses Python's built-in `sqlite3` module and does not require additional packages.

---

# Database Location

Place SQLite databases inside the `databases/` directory:

```text
databases/
├── example.db
├── users.sqlite
└── shop.sqlite3
```

The application can then discover the available databases automatically.

---

# Supported Database Files

The viewer supports common SQLite database extensions:

```text
.db
.sqlite
.sqlite3
```

---

# Read-Only Viewer

This project is intended to be a **database viewer**.

The application does not provide:

- SQL query input
- Record editing
- Record deletion
- Table creation
- Table modification
- Database modification

The goal is to provide a simple way to **inspect existing SQLite databases safely**.

---

# Security

The Flask version should preferably be used locally or behind appropriate authentication.

Do not expose databases containing sensitive information to an untrusted network.

For additional safety, database connections can be opened in read-only mode.

---

# Roadmap

- [ ] Database auto-discovery
- [ ] Table browser
- [ ] Schema viewer
- [ ] Record pagination
- [ ] Column sorting
- [ ] Record search
- [ ] CSV export
- [ ] JSON export
- [ ] Database statistics
- [ ] Dark mode
- [ ] Read-only database connections
- [ ] Docker support

---

# Requirements

### CLI

```text
Python 3.9+
```

No external dependencies are required.

### Flask

```text
Python 3.9+
Flask
```

---

---

# Author

**Your Name**

GitHub: `https://github.com/USERNAME`

---

⭐ If you find this project useful, consider giving it a star!
