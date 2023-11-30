#!/usr/bin/python3
import importlib.util

if __name__ == "__main__":
    # Convert machine code to human code
    spec = importlib.util.spec_from_file_location("hidden_4", "hidden_4.pyc")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    # Remove double underscore
    names = []
    for name in dir(module):
        if "__" not in name:
            names.append(name)
    # Print all the names defined after sorting
    for name in sorted(names):
        print(name)
