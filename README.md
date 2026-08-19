# 🐧 Linux Programs

A collection of **Linux programs, scripts, commands, and system utilities** created while learning and experimenting with Linux programming.

The goal of this repository is to understand how Linux works under the hood and practice interacting with the operating system through code.

---

## 📌 What's Inside?

This repository contains multiple projects and experiments covering:

* 🖥️ Linux system programming
* 📂 File & directory operations
* ⚙️ Process management
* 🔄 Signals
* 🧵 Threads
* 🔐 Permissions & users
* 🌐 Networking
* 📡 System information utilities
* ⌨️ Terminal-based applications
* 🐚 Shell scripting
* 🐍 Python utilities
* 🧪 Linux experiments and practice programs

The repository is continuously evolving as new programs and projects are added.

---

## 🛠️ Technologies

| Technology | Purpose                            |
| ---------- | ---------------------------------- |
| 🐧 Linux   | Operating System                   |
| C          | System Programming                 |
| C++        | Programming & DSA                  |
| Bash       | Shell Scripting                    |
| Python     | Automation & Terminal Applications |
| Git        | Version Control                    |

---

# 🚀 Projects

This repository contains multiple projects at different stages of development.

## 📋 Terminal Todo Manager

**Status:** 🟡 Working On

A terminal-based Todo application built with **Python and Textual**.

The goal is to build a useful terminal application while learning how to create interactive TUI applications and work with structured data.

### Current Features

* [x] Load todos from JSON
* [x] Display todo categories
* [x] Display todo titles
* [x] Filter todos by category
* [x] Interactive category selection
* [x] Terminal user interface using Textual
* [ ] Add new todos
* [ ] Edit todos
* [ ] Delete todos
* [ ] Mark todos as completed
* [ ] Priority filtering
* [ ] Due-date handling
* [ ] Persistent updates to `todo.json`

### Current Structure

```text
todo-manager/
│
├── app.py
├── sidebar.py
├── content.py
├── todo.json
└── ...
```

The project is currently being developed and will gradually become a more complete terminal-based Todo application.

---

## 📁 Other Projects

More Linux programs and experiments are being added to this repository.

Projects may include:

* 🗂️ File management utilities
* ⚙️ Process management programs
* 🔄 Signal handling programs
* 🧵 Threading experiments
* 🌐 Networking applications
* 🐚 Shell scripts
* 📡 System information utilities
* ⌨️ Terminal applications
* 🧪 Linux system programming experiments

> Projects will be documented here as they become more complete.

---

# 📂 Repository Structure

The structure may evolve as new projects are added.

```text
linux-programs/
│
├── file-management/
│   ├── create_file.c
│   ├── read_file.c
│   └── copy_file.c
│
├── processes/
│   ├── fork.c
│   ├── exec.c
│   └── wait.c
│
├── signals/
│   ├── signal.c
│   └── sigaction.c
│
├── threads/
│   ├── pthread.c
│   └── mutex.c
│
├── networking/
│   ├── client.c
│   └── server.c
│
├── shell-scripting/
│   ├── backup.sh
│   └── system-info.sh
│
├── todo-manager/
│   ├── app.py
│   ├── sidebar.py
│   ├── content.py
│   └── todo.json
│
└── README.md
```

---

# 🚀 Getting Started

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/linux-programs.git
cd linux-programs
```

---

## C Programs

Compile:

```bash
gcc program.c -o program
```

Run:

```bash
./program
```

For POSIX threads:

```bash
gcc program.c -o program -pthread
```

---

## C++ Programs

Compile:

```bash
g++ program.cpp -o program
```

Run:

```bash
./program
```

---

## Bash Scripts

Make the script executable:

```bash
chmod +x script.sh
```

Run:

```bash
./script.sh
```

---

## Python Projects

Run a Python program:

```bash
python3 program.py
```

For the Textual Todo Manager, install the dependency:

```bash
pip install textual
```

Then run:

```bash
python3 app.py
```

---

# 🎯 Learning Goals

The main goal of this repository is to learn Linux by **building programs rather than only reading about concepts**.

```text
Linux
 ├── Processes
 ├── Files
 ├── Memory
 ├── Threads
 ├── Signals
 ├── IPC
 ├── Networking
 ├── Permissions
 ├── System Calls
 └── Terminal Applications
```

Each project is an opportunity to understand a different part of the Linux operating system.

---

# 📚 Topics Roadmap

## 🟢 Beginner

* [ ] Linux commands
* [ ] File handling
* [ ] Directory handling
* [ ] Environment variables
* [ ] Permissions
* [ ] Shell scripting

## 🟡 Intermediate

* [ ] `fork()`
* [ ] `exec()`
* [ ] `wait()`
* [ ] Signals
* [ ] Pipes
* [ ] Named pipes
* [ ] Shared memory
* [ ] Message queues
* [ ] Threads
* [ ] Mutexes

## 🔴 Advanced

* [ ] Socket programming
* [ ] TCP/UDP
* [ ] Linux system calls
* [ ] `/proc` filesystem
* [ ] `/sys` filesystem
* [ ] Daemons
* [ ] Linux utilities
* [ ] System monitoring tools
* [ ] Terminal UI applications

---

# 💡 Future Project Ideas

Some larger projects that can eventually be built from these concepts:

* 🖼️ Terminal Wallpaper Manager
* 📊 Network Speed Monitor
* 💻 System Resource Monitor
* 🌐 Network Scanner
* 📁 Terminal File Manager
* 🔥 Process Manager
* 📝 Terminal Text Editor
* 📡 TCP/UDP Chat Application
* 🐚 Mini Shell
* 📋 Terminal Todo Manager

---

# 🧠 Philosophy

> **Don't just use Linux — understand how it works.**

Every program in this repository is an opportunity to understand the Linux operating system more deeply.

The focus is on:

```text
Learning
   ↓
Building
   ↓
Breaking
   ↓
Debugging
   ↓
Understanding
```

---

# 📈 Progress

```text
Linux Programming Journey

████████░░░░░░░░░░░░  40%

Learning → Building → Breaking → Debugging → Understanding
```

Progress will be updated as new concepts and projects are completed.

---

# 🤝 Contributions

This is primarily a personal learning repository, but suggestions, improvements, and interesting Linux programming ideas are always welcome.

---

# ⭐ Support

If you find this repository useful, consider giving it a ⭐.

---

> 🚧 **This repository is actively being developed.**
>
> New Linux programs, experiments, and larger projects will be added over time.
