import os
import os.path as paths

def exists(file):
    return paths.isfile(file) and os.access(file, os.R_OK)
