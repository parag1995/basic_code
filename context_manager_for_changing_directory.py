import os
from contextlib import contextmanager


@contextmanager
def chg_dir(destination):
    try:
        cwd = os.getcwd()
        os.chdir(destination)
        yield
    finally:
        os.chdir(cwd)

with chg_dir('x_dir'):
    print(os.listdir())
