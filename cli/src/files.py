import os
import os.path as paths

def exists(path):
    dir_exists = paths.isdir(path)
    readable_file = paths.isfile(path) and os.access(path, os.R_OK)
    return dir_exists or readable_file

def is_empty(dir_path):
    return os.listdir(dir_path) == []

def remove(path):
    os.remove(path)
