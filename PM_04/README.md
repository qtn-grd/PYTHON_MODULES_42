## 📖 Module 04 — Data Archives

**Digital Preservation Division of Ancient Knowledge**

This module focuses on file handling in Python, as well as the different input and output streams used within the terminal environment.

### Concepts Covered

* `open()` / `read()` / `close()`
* Standard input / output / error (`stdin`, `stdout`, `stderr`)
* `with` statement
* Context managers


## Questions


### Q. 1

What is the type of the data returned by open()?

### R. 1

The object returned by open() is usually of type `io.TextIOWrapper` in text mode.

To check it, try the following code:

    f = open("file.txt", "r")
    print(type(f))

to obtain:

    <class '_io.TextIOWrapper'>

