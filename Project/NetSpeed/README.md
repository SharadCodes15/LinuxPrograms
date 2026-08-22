# NETSPEED

A fast, lightweight Linux terminal network-speed monitor built with **Python** and **Textual**.

NETSPEED provides a live terminal UI for monitoring network performance without leaving your command line.

## Features

* 🚀 Real-time network speed monitoring
* 📥 Download speed display
* 📤 Upload speed display
* 📊 Live bandwidth statistics
* 🖥️ Interactive terminal UI powered by Textual
* 🐧 Designed for Linux
* ⚡ Lightweight and easy to run
* ⌨️ Keyboard-friendly interface

## Requirements

* Linux
* Python 3.10+
* `pip`
* A terminal with Unicode/ANSI support

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/netspeed.git
cd netspeed
```

Create a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

If Textual is the only dependency, you can install it directly:

```bash
pip install textual
```

## Usage

Start NETSPEED with:

```bash
python3 netspeed.py
```

Or, if the project provides an executable entry point:

```bash
./netspeed
```

The application will open an interactive terminal interface and continuously display current network activity.

## Controls

| Key | Action                     |
| --- | -------------------------- |
| `q` | Quit NETSPEED              |
| `r` | Refresh/restart monitoring |
| `c` | Clear statistics           |

> Controls may vary depending on the current implementation.

## Example

```text
╭──────────────────── NETSPEED ────────────────────╮
│                                                  │
│   DOWNLOAD                 UPLOAD                │
│   12.84 MB/s               2.31 MB/s             │
│                                                  │
│   ↓██████████████████░░░░   ↑██████░░░░░░░░░░    │
│                                                  │
│   Interface: eth0                                │
│   Status: Connected                              │
│                                                  │
╰──────────────────────────────────────────────────╯
```

## Project Structure

```text
netspeed/
├── netspeed.py
├── requirements.txt
├── README.md
└── LICENSE
```

For a larger application, the project can be organized as:

```text
netspeed/
├── netspeed/
│   ├── __init__.py
│   ├── app.py
│   ├── network.py
│   └── widgets.py
├── requirements.txt
├── README.md
└── LICENSE
```

## How It Works

NETSPEED periodically reads network interface statistics from Linux and calculates the amount of data transferred between updates.

The basic calculation is:

```text
speed = bytes_transferred / elapsed_time
```

The result is converted into human-readable units such as:

```text
B/s
KB/s
MB/s
GB/s
```

Textual handles the terminal interface, reactive updates, widgets, keyboard input, and screen rendering.

## Dependencies

The project uses:

* **Python** — application runtime
* **Textual** — terminal user interface framework
* Linux network statistics — network monitoring

Additional Python packages may be required depending on how network statistics are collected.

## Development

Clone the project and create a development environment:

```bash
git clone https://github.com/yourusername/netspeed.git
cd netspeed

python3 -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
```

Run the application:

```bash
python3 netspeed.py
```

## Contributing

Contributions are welcome.

1. Fork the repository.
2. Create a feature branch.
3. Make your changes.
4. Test the application on Linux.
5. Submit a pull request.

Please keep the UI responsive and avoid blocking the Textual event loop.


## Author

**Sharad Codes**

Replace this section with your name, GitHub profile, or project organization.

---

⭐ If you find NETSPEED useful, consider giving the project a star!
