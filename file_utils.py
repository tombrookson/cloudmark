
import os

def read_file(file):
    if not os.path.isfile(file):
        raise FileNotFoundError(f"The file {file} does not exist.")
    
    try:
        with open(file, "r") as f:
            return f.read()
    except Exception as e:
        raise IOError(f"Error reading file {file}: {e}")