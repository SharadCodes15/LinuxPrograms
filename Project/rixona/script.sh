#! /usr/bin/bash
execute() {
  echo "Executing script..."
  mkdir -p src/unipm/{core,backends,features,ui}
mkdir -p tests
touch src/unipm/__init__.py
touch src/unipm/main.py

touch src/unipm/core/__init__.py
touch src/unipm/core/detector.py
touch src/unipm/core/executor.py
touch src/unipm/core/router.py
touch src/unipm/core/config.py

touch src/unipm/backends/__init__.py
touch src/unipm/backends/base.py
touch src/unipm/backends/apt.py
touch src/unipm/backends/pacman.py
touch src/unipm/backends/yay.py
touch src/unipm/backends/paru.py
touch src/unipm/backends/flatpak.py

touch src/unipm/features/__init__.py
touch src/unipm/features/history.py
touch src/unipm/features/backup.py
touch src/unipm/features/cleanup.py
touch src/unipm/features/updates.py
touch src/unipm/features/health.py

touch src/unipm/ui/__init__.py
touch src/unipm/ui/terminal.py

touch tests/test_detector.py
touch tests/test_router.py

touch README.md
touch .gitignore
tree -I '.venv|__pycache__|.pytest_cache'
}
execute