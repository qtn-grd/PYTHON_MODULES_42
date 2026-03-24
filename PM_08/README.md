## 🧩 Module 08 — The Matrix

**Welcome to the Real World of Data Engineering**

This module revisits Python import management by exploring how to download and manage external packages, use virtual environments, retrieve system information from the OS, and secure data when sharing projects.

### Concepts Covered

* venv
* sys.executable
* sys.prefix / sys_base.prefix
* pip
* requirements.txt
* poetry
* numpy
* pandas
* matplot
* requests
* .toml
* .env
* load_dotenv
* .gitignore

<details>
<summary> 😶‍🌫️ DETAILED EXPLANATIONS</summary>

### ex0

#### Descriptions

- sys.executable :

A string giving the absolute path of the executable binary for the Python interpreter, on systems where this makes sense. If Python is unable to retrieve the real path to its executable, sys.executable will be an empty string or None.

- sys.prefix

A string giving the site-specific directory prefix where the platform independent Python files are installed; on Unix, the default is /usr/local. This can be set at build time with the --prefix argument to the configure script. See Installation paths for derived paths.

- sys.base_prefix

Equivalent to prefix, but referring to the base Python installation.

When running under virtual environment, prefix gets overwritten to the virtual environment prefix. base_prefix, conversely, does not change, and always points to the base Python installation. Refer to Virtual Environments for more information.


#### Commands 

- outside

python3 loading.py

- inside

python3 -m venv matrix_env
source matrix_env/bin/activate
python3 loading.py
deactivate
rm -r matrix_env

#### Resume

This exercise introduces the concept of a virtual environment (venv), which is an essential foundation of modern Python. It highlights the distinction between a system’s global environment and a project-specific, isolated environment. The script uses `sys.prefix` and `sys.base_prefix` to detect whether Python is running in a venv, which is an important internal mechanism.

It explores system concepts like `sys.executable` (the path to the Python interpreter) and `site-packages` (where dependencies are installed). The goal is to understand that each project must have its own execution space to avoid conflicts between dependencies.

There are essential commands: `python -m venv`, `activate`, and `deactivate`

---

### ex01

#### Descriptions

- numpy

The NumPy library (http://www.numpy.org/) allows numerical computations with Python. It introduces simplified handling of numerical arrays.

To use NumPy, it is necessary to be in an environment that includes this library; see Introduction to Python.

- pandas

pandas is a Python package that provides fast, flexible, and expressive data structures designed to make working with "relational" or "labeled" data both easy and intuitive. It aims to be the fundamental high-level building block for doing practical, real-world data analysis in Python. Additionally, it has the broader goal of becoming the most powerful and flexible open-source data analysis/manipulation tool available in any language. It is already well on its way towards this goal.

- matplot

Matplotlib produces publication-quality figures in a variety of hardcopy formats and interactive environments across platforms. Matplotlib can be used in Python scripts, Python/IPython shells, web application servers, and various graphical user interface toolkits.

- requests

Python requests is a widely used library that allows sending HTTP requests and handling their responses. Although `.get()` is the most commonly used method, the module provides many additional options.

#### Commands 

- EMPTY VENV

python3 -m venv empty_env
source empty_env/bin/activate
python3 loading.py
deactivate

- PIP VENV

python3 -m venv pip_env
source pip_env/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
python3 loading.py
deactivate

- POETRY VENV

python3 -m venv poetry_env
source poetry_env/bin/activate
pip install poetry
poetry install --no-root
python3 loading.py
deactivate

#### Resume

This exercise demonstrates the transition from “Python alone” to “Python with its ecosystem.” It covers managing external dependencies such as pandas, numpy, matplotlib, and requests.

The exercise highlights pip (the package manager) and requirements.txt, which allow an environment to be reproduced identically. In parallel, it introduces Poetry, a modern alternative that centralizes dependencies, environment, and configuration in pyproject.toml.

On the code side, importlib is used to dynamically detect the presence of modules, introducing a more robust programming approach (error handling, missing dependencies).

The exercise uses:

- HTTP APIs with requests  
- numerical data with numpy  
- dataframes with pandas  
- visualization with matplotlib  


---

### ex02

#### Descriptions

- python-dotenv 

It reads key-value pairs from a .env file and can set them as environment variables. It helps in the development of applications following the 12-factor principles.

#### Commands 

- python3 -m venv oracle_env
- source oracle_env/bin/activate
- python3 oracle.py -> Error missing Module
- pip install python-dotenv
- python3 oracle.py
- cp -r .env.example .env
- python3 oracle.py

To override, enter a new key value directly in the terminal line and execute the command immediately after.


#### Resume


This exercise teaches how to separate code from its configuration, which is an essential practice in production environments. Environment variables are used to store sensitive or environment-specific information (API keys, URLs, dev/prod mode).

It introduces python-dotenv, which allows loading a .env file during development. This avoids hardcoding secrets in the code, which is a critical bad practice.

A robust configuration system is implemented using:

- os.getenv() to read variables  
- parameter validation  
- different behavior depending on the environment (development vs production)  

It also covers security concepts:

- never versioning .env (via .gitignore)  
- detecting unsafe default values  
- allowing overrides via the system  

Conceptually, it introduces:

- external configuration of an application  
- secrets management  
- the difference between development and production environments  

This is a key step toward real-world applications connected to external services.


### SRCS :

- https://www.digibeatrix.com/python/en/environment-management/python-package-management-pip-venv-poetry-guide/?utm_source=chatgpt.com

- https://python.land/virtual-environments?utm_source=chatgpt.com

- https://www.geeksforgeeks.org/python/managing-virtual-environments-in-python-poetry/

</details>