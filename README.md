# 🐧 Linux Programs

> **Learn Linux by doing.**
> A practical collection of Linux commands, programs, shell scripts, and hands-on exercises.

---

## 📌 About

This repository contains my **Linux learning and practice programs**, covering everything from basic terminal commands to scripting, file management, processes, permissions, networking, and system utilities.

The goal is simple:

**Learn → Practice → Build → Automate 🚀**

---

## 📚 Topics Covered

* 🗂️ File & Directory Management
* 🔐 File Permissions & Ownership
* 🔎 File Searching with `find`
* 📝 Text Processing with `grep`, `sed`, `awk`
* 📦 Archiving with `tar`
* ⚙️ Process Management
* 💾 Disk & Storage Management
* 🌐 Networking Commands
* 🐚 Shell Scripting
* 📜 Command History
* 🔧 System Utilities
* 🚀 Linux Automation

---

## 🧪 Practice Examples

```bash
# Create directories
mkdir -p project/src project/docs project/bin

# Search for files
find ~ -type f -name "*.txt" -mtime -3

# Change permissions
chmod 744 script.sh

# Create compressed archive
tar -czvf project.tar.gz project

# Search logs
grep -i "error" *.log

# Check running processes
ps aux | grep "[f]irefox"

# Check disk usage
du -sh ~
df -h

# Test network connectivity
ping google.com

# View command history
history | tail -20
```

---

## 📁 Repository Structure

```text
linux-programs/
│
├── basics/
│   ├── file-management/
│   ├── permissions/
│   └── commands/
│
├── shell-scripting/
│   ├── basics/
│   └── advanced/
│
├── process-management/
│
├── networking/
│
├── file-handling/
│
└── README.md
```

> The structure may evolve as more Linux concepts and programs are added.

---

## 🎯 Goals

* Build strong Linux fundamentals
* Become comfortable with the terminal
* Learn shell scripting
* Understand Linux system administration concepts
* Practice real-world Linux commands
* Automate repetitive tasks
* Build useful Linux utilities

---

## 🛠️ Requirements

A Linux environment is recommended.

You can use:

* 🐧 Arch Linux
* 🐧 Ubuntu
* 🐧 Debian
* 🐧 Fedora
* 🐧 Linux Mint
* 🪟 WSL

Basic tools used throughout the repository include:

```bash
bash
coreutils
grep
find
tar
ps
df
du
ping
traceroute
```

---

## 🚀 Getting Started

Clone the repository:

```bash
git clone https://github.com/YOUR-USERNAME/linux-programs.git
```

Enter the repository:

```bash
cd linux-programs
```

Run a program or script:

```bash
chmod +x script.sh
./script.sh
```

---

## 📈 Learning Path

```text
Linux Basics
     ↓
Files & Directories
     ↓
Permissions
     ↓
Processes
     ↓
Text Processing
     ↓
Networking
     ↓
Shell Scripting
     ↓
Automation
     ↓
Advanced Linux
```

---

## 💡 Philosophy

> **Don't just memorize Linux commands — understand what they do and use them to build something.**

Every program in this repository is intended to be **Educational ,practical, understandable, and useful for hands-on learning**.

---

## ⭐ Support

If this repository helps you learn Linux, consider giving it a ⭐.
