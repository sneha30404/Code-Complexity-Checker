# Code Complexity Checker

[![PyPI](https://img.shields.io/pypi/v/code-complexity-checker.svg)](https://pypi.org/project/code-complexity-checker/)
[![Python](https://img.shields.io/badge/python-3.7%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

A lightweight Python tool that **analyzes the complexity** of your code using [Radon](https://radon.readthedocs.io/) . Quickly check function complexity, detect high-complexity areas, and improve your code quality! 

## Features
- **Analyze Cyclomatic Complexity** of Python functions & classes  
- **Generate JSON Reports** with detailed complexity insights  
- **Command-Line Interface (CLI)** for quick execution  
- **Lightweight & Easy to Use**  
- **Supports Python 3.7+**

## Installation
Install the package using `pip`:
```bash
pip install code-complexity-checker
```

## Usage
Analyze a Python file:
```bash
!code-checker --file example.py
```
This will output something like:
```bash
[
    {"function": "calculate_factorial", "complexity": 3, "lineno": 5},
    {"function": "fibonacci", "complexity": 4, "lineno": 12}
]
```

## How It Works

1. Reads the Python file
2. Uses **Radon's `ComplexityVisitor`** to analyze function/class complexity
3. Outputs a structured JSON report with function names & their complexity scores


## Why Use This?

- Helps you **identify complex functions** early  
- Makes code **easier to maintain & optimize**  
- Great for **code reviews & refactoring** 

## Contributing
Contributions are welcome! Follow these steps to contribute:

1. Fork the repository on [GitHub](https://github.com/sneha30404/code-complexity-checker).
2. Clone your fork:
   ```bash
   git clone https://github.com/sneha30404/code-complexity-checker.git
    ```
3. Create a new branch for your feature
    ```bash
    git checkout -b feature-name
    ```
4. Make your changes and commit them:
    ```bash
    git commit -m "Add feature-name"
    ```
5. Push to your branch:
    ```bash
    git push origin feature-name
    ```
6. Submit a Pull Request.


## Links

- **PyPI:** [Code Complexity Checker](https://pypi.org/project/code-complexity-checker/)  
- **GitHub:** [Source Code](https://github.com/sneha30404/code-complexity-checker/)  
- **Radon Docs:** [Radon Library](https://radon.readthedocs.io/)  

---

## License

This project is licensed under the **MIT License**.

---

**Happy Coding!** 