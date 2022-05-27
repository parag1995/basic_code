from contextlib import contextmanager

@contextmanager
def open_file(file, mode):
    try:
        f = open(file,mode)
        yield f
    finally:
        f.close()

with open_file('sample.txt','w') as f:
    f.write('this is update on smaple.txt using decorators')

print(f.closed)