from importlib import util, import_module
from typing import Dict, Tuple, Optional


def check_dependencies() -> Dict[str, Tuple[bool, Optional[str]]]:
    """
    Check if required Python packages are installed.

    Returns:
        A dictionary mapping package name to a tuple:
        (installed: bool, version: str or None)
    """

    packages: list[str] = ["pandas", "numpy", "matplotlib", "requests"]

    dep_status: Dict[str, Tuple[bool, Optional[str]]] = {}

    for package in packages:
        module_spec = util.find_spec(package)
        if module_spec is None:
            dep_status[package] = (False, None)
        else:
            module = import_module(package)
            version = getattr(module, "__version__", "unknown")
            dep_status[package] = (True, version)

    return dep_status


def display_status(dep_status: Dict[str, Tuple[bool, Optional[str]]]) -> bool:
    """
    Display the installation status of packages.

    Args:
        dep_status: Dictionary from check_dependencies().

    Returns:
        True if all dependencies are installed, False otherwise.
    """

    all_ok = True

    print()
    print("Checking dependencies:")

    package_messages = {
        "pandas": "Data manipulation ready",
        "numpy": "Numerical computations ready",
        "matplotlib": "Visualization ready",
        "requests": "Network access ready",
    }

    for package, (installed, version) in dep_status.items():
        if installed and version is not None:
            msg = package_messages.get(package, "ready")
            print(f"[OK] {package} ({version}) - {msg}")
        else:
            print(f"[KO] {package} not installed")
            all_ok = False

    return all_ok


def run_analysis() -> None:
    """
    Run the data analysis pipeline:
    - Fetch data from an API (fallback to random data if unavailable)
    - Process data with pandas and numpy
    - Visualize results with matplotlib
    - Save visualization to 'matrix_analysis.png'
    """

    import numpy as nump
    import pandas as pand
    import matplotlib.pyplot as matplot

    data = None

    try:
        import requests

        url = "https://api.coindesk.com/v1/bpi/currentprice.json"

        response = requests.get(url, timeout=5)
        response.raise_for_status()
        value = float(response.json()["bpi"]["USD"]["rate"].replace(",", ""))
        data = nump.full(1000, value)
        print("Data fetched from API.")

    except Exception:
        print("\t-> Could not fetch external data, "
              "generating local data instead.")
        data = nump.random.rand(1000)

    data_frame = pand.DataFrame(data, columns=["matrix_points"])

    print()
    print("Processing 1000 data points...")
    print()
    print(data_frame.describe())

    matplot.figure()
    data_frame["matrix_points"].plot(title="Matrix Data Analysis")

    matplot.xlabel("Index")
    matplot.ylabel("Value")

    print()
    print("Generating visualization...")
    print()

    matplot.savefig("matrix_analysis.png")
    matplot.close()


def main() -> None:
    """
    Main function to check dependencies and run the analysis pipeline.
    """

    print()
    print("LOADING STATUS: Loading programs...")

    dep_status = check_dependencies()
    all_is_fine = display_status(dep_status)

    if not all_is_fine:
        print()
        print("Install missing dependencies with pip or Poetry and run again.")
        return

    print()
    print("Analyzing Matrix data...")

    run_analysis()

    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")


if __name__ == "__main__":
    main()
