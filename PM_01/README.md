## 🌺 Module 01 — CodeCultivation 

**Object-Oriented Garden Systems**

This module introduces core object-oriented programming concepts, including classes, nested classes, encapsulation and inheritance. It also explores different ways to access and use Python `.py` files.

### Concepts Covered

* Shebang
* Docstrings
* Factory pattern
* Encapsulation
* Inheritance
* Nested classes
* Instance methods
* Static methods
* Class methods

### Questions

#### Q.1

What is the purpose of `if __name__ == "__main__"` in a Python file?

#### R.1

t checks whether the file is being run directly or imported as a module.
When executed directly, `__name__` is set to `"__main__"`.
This allows to run test code or a main function only in that case.
If the file is imported, the block is skipped.
It helps separate reusable code from execution logic.

#### Q.2

What is a shebang? What is it used for?

#### R.2

A shebang is the first line of a script _(`#!/usr/bin/env python3`)_.
It tells the system which interpreter to use to execute the file.
It allows the script to be run directly without explicitly calling Python.