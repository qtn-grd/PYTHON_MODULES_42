## 🧙 Module 10 - FuncMage

**Master the Ancient Arts of Functional Programing**

This module covers various advanced concepts in Python OOP, aimed at defining, storing, reusing, and adapting functions, with a strong emphasis on adaptability and data security.

### Concepts Covered

* `lambda`
* `Callable`
* *args
* **kwargs
* higher-order / first-class citizen
* closure
* lexical scope
* non-local
* functools
* decorator

### Functions Explored

* map()
* reduce()
* lru_cache()
* perf_counter()

### Sources

- https://www.w3schools.com/python/python_lambda.asp
- https://realpython.com/python-lambda/
- https://www.learnpython.org/fr/Closures
- https://zestedesavoir.com/tutoriels/954/notions-de-python-avancees/2-functions/3-decorators/


### Questions

#### Q.1

How do lambda expressions make code more concise? When should you use lambda vs. regular function definitions?

#### R.1

Lambda expressions make code more concise by allowing the creation of small, anonymous functions in a single line.
They are useful for simple, one-time operations, especially with functions like map, filter, or sorted.
However, for more complex logic, reusable code, or better readability, regular function definitions should be preferred.

#### Q.2

How do higher-order functions enable code reuse and composition?
What makes functions "first-class citizens" in Python?

#### R.2

Higher-order functions enable code reuse by allowing functions to be passed as arguments and reused in different contexts. They also enable composition by combining simple functions into more complex behaviors.

In Python, functions are first-class citizens because they can be assigned to variables, passed as arguments, returned from other functions, and stored in data structures, just like any other object.

#### Q.3

From which package is it recommended to use Callable ? Whats is the
purpose of callable() ?

#### R.3

It is recommended to import Callable from collections.abc in modern Python.

Callable is used for type hinting to specify that an object is a function and optionally define its input and output types.

The built-in function callable() is used at runtime to check whether an object can be called like a function.

#### Q.4

How do closures enable functions to "remember" their creation
environment? What are the benefits of lexical scoping in functional
programming?

#### R.4

Closures allow functions to remember their creation environment by capturing variables from their enclosing scope. These variables remain accessible even after the outer function has finished execution.

This is possible thanks to lexical scoping, where functions retain access to variables defined in their original context.

The benefits include better encapsulation, avoiding global variables, improved modularity, and the ability to maintain state across function calls.

#### Q.5

Why is global forbidden, but nonlocal allowed ? What are the key
differences ?

#### R.5

`global` is discouraged because it modifies variables at the module level, leading to unpredictable side effects and poor code maintainability.

`nonlocal`, on the other hand, is used to modify variables in an enclosing function scope, which keeps the state localized and controlled.

The key difference is that global affects the entire program, while nonlocal only affects a specific lexical scope, making it safer and more appropriate for closures.

#### Q.6

How does functools.reduce enable powerful data aggregation? What
are the performance benefits of memoization with lru_cache?

#### R.6

functools.reduce enables powerful data aggregation by applying a function cumulatively to a sequence, reducing it to a single value. It allows flexible and reusable aggregation logic by simply changing the operation function.

Memoization with lru_cache improves performance by storing previously computed results and avoiding redundant calculations. This is especially beneficial for recursive functions, reducing time complexity significantly.

#### Q.7

How do decorators enable separation of concerns? What’s the
difference between @staticmethod and regular instance methods?

#### R.7

Decorators enable separation of concerns by allowing additional behavior, such as logging, validation, or retry logic, to be added without modifying the original function. This keeps the core logic clean and modular.

A regular instance method operates on an instance and has access to self, allowing it to interact with object state. A @staticmethod does not receive self and behaves like a regular function that belongs to the class namespace but does not depend on instance data.