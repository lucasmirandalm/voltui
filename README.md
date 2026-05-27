# VoltUI

<p align="center">
  <strong>A colorful terminal battery monitor built with Python.</strong>
</p>

<p align="center">
  <img src="assets/voltui-demo.gif" alt="VoltUI demo" width="700">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python" alt="Python">
  <img src="https://img.shields.io/badge/Terminal-UI-green?style=for-the-badge" alt="Terminal UI">
  <img src="https://img.shields.io/badge/Made%20with-Rich-purple?style=for-the-badge" alt="Rich">
  <img src="https://img.shields.io/badge/Tests-Pytest-yellow?style=for-the-badge" alt="Pytest">
</p>

---

## About

**VoltUI** is a simple and colorful terminal application that displays your laptop battery status in real time.

It shows a clean ASCII battery, the current battery percentage, the remaining battery time, and a charging indicator when your device is plugged in.

The interface changes color automatically based on the current battery level.

---

## Features

- Real-time battery monitoring
- Colorful terminal interface
- Dynamic battery colors
- Charging status animation
- Remaining battery time
- Centered terminal layout
- Clean project structure
- Simple unit tests
- Lightweight and easy to run

---

## Battery Colors

| Battery Level | Color |
| --- | --- |
| 51% - 100% | Green |
| 26% - 50% | Yellow |
| 0% - 25% | Red |

---

## Demo

<p align="center">
  <img src="assets/voltui-demo.gif" alt="VoltUI running in the terminal" width="700">
</p>

---

## Project Structure

```txt
voltui/
├── main.py
├── config.py
├── battery.py
├── ui.py
├── requirements.txt
├── requirements-dev.txt
├── README.md
└── tests/
    └── test_battery.py
```

---

## Requirements

- Python 3.10+
- psutil
- rich

For development and testing:

- pytest

---

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/voltui.git
```

Enter the project folder:

```bash
cd voltui
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment:

```bash
source .venv/bin/activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

Run VoltUI:

```bash
python main.py
```

To stop the application, press:

```bash
Ctrl + C
```

---

## Running Tests

Install the development dependencies:

```bash
pip install -r requirements-dev.txt
```

Run the test suite:

```bash
pytest
```

VoltUI includes simple unit tests for the core battery logic:

- battery color rules
- remaining time formatting
- battery data handling

The terminal interface itself is not heavily tested because it is mainly visual and rendered through Rich.

---

## Dependencies

VoltUI uses:

- [psutil](https://pypi.org/project/psutil/) to read battery information
- [Rich](https://pypi.org/project/rich/) to render the terminal interface
- [pytest](https://pypi.org/project/pytest/) to run automated tests

---

## Why I built this

I built VoltUI as a small Python terminal project to practice:

- Python project organization
- Working with external libraries
- Terminal UI design
- Real-time terminal updates
- Clean code structure
- Writing simple automated tests

---

## Roadmap

Possible future improvements:

- Add command-line options
- Add custom themes
- Add compact mode
- Add battery notifications
- Add battery history tracking
- Package VoltUI as an installable CLI tool
- Add GitHub Actions for automated testing

---

## License

This project is open source and available under the MIT License.

---

<p align="center">
  Made with Python and a little bit of terminal magic.
</p>