# Contributing Guidelines

Thank you for your interest in contributing to this project!

## How to Contribute

1. **Fork the repository** and create your branch from `main`.
2. **Clone your fork** and set up the project locally (see README for setup instructions).
3. **Create clear, focused commits** with descriptive messages.
4. **Follow code style guidelines:**
   - Use Python type hints.
   - Run `make lint-check` and `make lint-fix` before submitting.
5. **Test your changes** to ensure nothing is broken.
6. **Open a Pull Request** with a clear description of your changes and reference any related issues.

## Code of Conduct
- Be respectful and constructive in all communications.
- Provide helpful feedback and be open to suggestions.

## Reporting Issues
- If you find a bug or have a feature request, please open an issue with clear steps to reproduce or describe your idea.

---

# Project Setup & Installation

Below are the steps and commands used to set up and run this project from scratch. These instructions summarize all setup and development environment preparations performed so far.

## 1. Clone the Repository
```
git clone <repo-url>
cd <repo-folder>
```

## 2. Python Environment & Dependencies
- Python 3.12 was used.
- [uv](https://github.com/astral-sh/uv) was used for virtual environment and dependency management.

```
pip install uv
uv venv .venv
source .venv/bin/activate
uv pip install -r requirements.txt
```

## 3. Node.js & Frontend
```
sudo apt-get update
sudo apt-get install -y nodejs npm
npm install
```

## 4. Django Database Setup
```
uv run python manage.py migrate
uv run python manage.py import_blog_data
```

## 5. Lint & Format
```
make lint-check
make lint-fix
```

## 6. Development Server
```
make dev
```

---

All these steps are also summarized in the README and Makefile. If you are working in a different environment (e.g., Windows), you may need to adapt the commands accordingly.
