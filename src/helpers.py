from pathlib import Path


def read_file(file_name: str) -> str:
    """Reads file and returns its contents as string"""
    file_path = Path() / file_name
    with open(file_path) as f:
        contents = f.read()
    return contents
