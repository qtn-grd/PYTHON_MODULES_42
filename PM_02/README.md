## 💂‍♂️ Module 02 — Garden Guardian

**Data Engineering for Smart Agriculture**

This module focuses on error handling in Python, including how to manage, structure, and define custom exceptions.

### Concepts Covered

* `try` / `except`
* `raise`
* `finally`
* Exceptions


### Questions

#### Q.1

Why does Python have different types of errors? How can you catch multiple types of errors with a single try: only?

#### R.1

Python has different error types to represent different failure causes precisely, making debugging and handling more accurate.
Each exception type signals a specific problem _(e.g., ValueError, TypeError)_.
This allows to react differently depending on the situation instead of using generic handling.
We can catch multiple errors in a single except by grouping them in a tuple.

#### Q.2

When should you create your own error types instead of using Python’s built-in ones? How does inheritance help organize different types of errors?

#### R.2

Creating custom error types is important when built-in exceptions are too generic and don’t clearly express a program’s domain logic.
They make the code more readable and allow more precise error handling.
Inheritance group related errors under a common base class.
It improves structure, clarity, and flexibility in large programs.

#### Q.3

Why is it important to clean up resources even when errors happen? How does the finally block help ensure cleanup always occurs?

#### R.3

When something breaks, files stay open, connections hang and memory leaks.

Cleaning up ensures resources are properly released and the system stays stable and predictable.

The finally block runs no matter what happens in the try block, error or not. Even if an exception is raised or caught, finally executes.

It guarantees that cleanup code always runs.