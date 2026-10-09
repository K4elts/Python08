import sys
import os
import site


def outside_environment() -> None:
    print()
    print("MATRIX STATUS: You're still plugged in")
    print()
    print(f"Current Python: {sys.executable}")
    print("Virtual Environment: None detected")
    print()
    print("WARNING: You're in the global environment!")
    print("The machine can see everything you install.")
    print()
    print("To enter the construct, run:")
    print("python -m venv matrix_env")
    print("source matrix_env/bin.activate # On Unix")
    print("matrix_env\\Scripts\\activate # On Windows")
    print()
    print("Then run this program again.")


def inside_environment() -> None:
    print()
    print("MATRIX STATUS: Welcome to the construct")
    print()
    print(f"Current Python: {sys.executable}")
    print("Virtual Environment: matrix_env")
    print()
    print(f"Environment Path: {sys.exec_prefix}")
    print()
    print("SUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting the global system")
    print()
    print("Package installation path:")
    print(f"{site.getsitepackages()}")


if __name__ == "__main__":
    print(f"{sys.executable}")
    print(f"{sys.base_prefix}")
    if sys.executable == sys.base_exec_prefix:
        outside_environment()
    else:
        inside_environment()
