# Terminal Project Manager

A modern **terminal-based project management application** built with **Python and Textual**.

Manage your projects and tasks directly from the terminal with a fast, keyboard-driven interface.

## ✨ Features

* 📁 Create and manage multiple projects
* ✅ Add, complete, and delete tasks
* 🔍 Search and filter tasks
* 💾 Persistent data storage
* ⌨️ Keyboard-first navigation
* 📊 Project progress tracking
* 🖥️ Beautiful terminal UI powered by Textual
* 🗄️ SQLite database support
* ⚡ Lightweight and fast

## 📸 Preview

```text
┌─────────────────────────────────────────────────────────────┐
│  PROJECT MANAGER                              [q] Quit      │
├──────────────────┬──────────────────────────────────────────┤
│ Projects         │  my-awesome-app                          │
│                  │                                           │
│ > my-app         │  Status: In Progress                     │
│   website        │                                           │
│   api-server     │                                           │
│                  │  Tasks                                    │
│                  │  ✓ Setup project                          │
│                  │  ✓ Create database                        │
│                  │  > Build authentication                   │
│                  │  □ Write tests                            │
│                  │                                           │
├──────────────────┴──────────────────────────────────────────┤
│ [a] Add task   [d] Delete   [Enter] Open   [q] Quit         │
└─────────────────────────────────────────────────────────────┘
```

## 🛠️ Tech Stack

* **Python 3.11+**
* **Textual** — terminal user interface
* **SQLite** — local data persistence
* **Rich** — terminal rendering and styling

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/terminal-project-manager.git
cd terminal-project-manager
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it:

### Linux / macOS

```bash
source .venv/bin/activate
```

### Windows

```powershell
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## 🚀 Usage

Start the application:

```bash
python main.py
```

Or, if the project is packaged as a module:

```bash
python -m project_manager
```

## ⌨️ Keyboard Shortcuts

| Key       | Action                   |
| --------- | ------------------------ |
| `↑` / `↓` | Navigate                 |
| `Enter`   | Open project             |
| `a`       | Add task                 |
| `d`       | Delete selected item     |
| `Space`   | Complete/uncomplete task |
| `/`       | Search                   |
| `n`       | New project              |
| `q`       | Quit                     |

## 📂 Project Structure

```text
terminal-project-manager/
│
├── project_manager/
│   ├── __init__.py
│   ├── app.py
│   ├── database.py
│   ├── models.py
│   ├── screens/
│   │   ├── __init__.py
│   │   ├── projects.py
│   │   └── tasks.py
│   └── widgets/
│       ├── __init__.py
│       ├── project_list.py
│       └── task_list.py
│
├── tests/
│   ├── test_database.py
│   └── test_models.py
│
├── main.py
├── requirements.txt
├── pyproject.toml
├── README.md
└── LICENSE
```

## 🗃️ Data Model

The application uses SQLite to store projects and tasks.

```text
Projects
├── id
├── name
├── description
├── status
└── created_at

Tasks
├── id
├── project_id
├── title
├── description
├── completed
├── priority
└── created_at
```

Each task belongs to a project, allowing the application to calculate project progress automatically.

## 🎯 Roadmap

* [x] Basic Textual interface
* [ ] Project creation
* [ ] Task creation
* [ ] Task completion
* [ ] SQLite persistence
* [ ] Search and filtering
* [ ] Project progress indicators
* [ ] Task priorities
* [ ] Due dates
* [ ] Tags
* [ ] Dark/light themes
* [ ] Export projects to Markdown
* [ ] Import/export JSON
* [ ] Git integration
* [ ] Configuration file
* [ ] Custom themes

## 🧪 Running Tests

Run the test suite with:

```bash
pytest
```

For coverage:

```bash
pytest --cov=project_manager
```

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a feature branch

```bash
git checkout -b feature/my-feature
```

3. Make your changes
4. Run the tests

```bash
pytest
```

5. Commit your changes

```bash
git commit -m "Add my feature"
```

6. Push your branch

```bash
git push origin feature/my-feature
```

7. Open a Pull Request

## 📄 License

This project is licensed under the **MIT License**. See [LICENSE](LICENSE) for details.

## 🌟 Why This Project?

Terminal Project Manager is designed as both a useful developer tool and a learning project for building **TUIs with Python**.

It demonstrates how to combine:

* Textual application architecture
* Reactive UI components
* Keyboard events
* SQLite databases
* Python application structure
* Terminal UX
* Automated testing

If you find the project useful, consider giving it a ⭐ on GitHub!
