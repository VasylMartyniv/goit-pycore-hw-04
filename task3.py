import sys
from pathlib import Path
from colorama import Fore, Style


def print_directory_structure(directory, indent=''):
    for item in directory.iterdir():
        if item.is_dir():
            print(Fore.BLUE + indent + item.name)
            print_directory_structure(item, indent + '    ')
        else:
            print(Fore.GREEN + indent + item.name)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python task3.py ./testdir")
        sys.exit(1)

    directory_path = Path(sys.argv[1])

    if not directory_path.exists() or not directory_path.is_dir():
        print("Invalid directory path.")
        sys.exit(1)

    print_directory_structure(directory_path)
