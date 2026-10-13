import importlib
from typing import Any


DEPENDENCIES = {
    "pandas": "Data manipulation ready",
    "numpy": "Numerical computation ready",
    "matplotlib": "Visualization ready"
}
MODULES: dict[str, Any] = {}


def check_dependencies() -> bool:
    all_dependencies = True
    print("Checking dependencies:")
    for package, description in DEPENDENCIES.items():
        try:
            module = importlib.import_module(package)
            MODULES[package] = module
            print(f"[OK] {package} ({module.__version__}) - {description}")
        except ImportError:
            print(f"[MISSING] '{package}' dependency")
            all_dependencies = False
    return all_dependencies


def compare_package_versions() -> None:
    print("Package versions:")
    for name, package in MODULES.items():
        version = getattr(package, "__version__", "unknown")
        print(f"{name}: {version}")


def show_install_instructions() -> None:
    print()
    print("To install dependencies:")
    print("Using pip:\n python3 -m pip install -r requirements.txt")
    print("Using Poetry:\n poetry install")


def generate_matrix_data() -> list[int]:
    np = MODULES["numpy"]
    print("Analyzing Matrix data...")
    data: list[int] = np.random.normal(loc=100, scale=15, size=1000)
    print(f"Processing {len(data)} data points...")
    return data


def analyze_matrix_data(data: list[int]) -> None:
    pandas = MODULES["pandas"]
    df = pandas.DataFrame(data, columns=["Energy"])
    print(df.head(5))
    print()
    print("Mean: ", df["Energy"].mean())
    print("Max: ", df["Energy"].max())
    print("Min: ", df["Energy"].min())


def visualize_matrix_data(data: list[int]) -> None:
    plt = importlib.import_module("matplotlib.pyplot")
    plt.plot(data)
    plt.title("Matrix Energy Analysis")
    plt.xlabel("Data point")
    plt.ylabel("Energy")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("matrix_analysis.png")
    plt.close()
    print()
    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")


def compare_pip_and_poetry() -> None:
    print()
    print("Pip:")
    print(
        " pip installs the flat list of packages in requirements.txt, "
        "with no automatic lock file."
    )
    print("Poetry:")
    print(
        " Poetry reads pyproject.toml, resolves the full dependency graph, "
        "and writes poetry.lock so installs are reproducible."
    )


if __name__ == "__main__":
    print()
    print("LOADING STATUS: Loading programs...")
    print()
    if not check_dependencies():
        show_install_instructions()
    else:
        compare_package_versions()
        print()
        data = generate_matrix_data()
        analyze_matrix_data(data)
        compare_pip_and_poetry()
        visualize_matrix_data(data)
