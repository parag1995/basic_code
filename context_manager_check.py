# context manager allows you to precisely allocate and deallocate resources whenever required,Most widely used example is with statement

class openfile:

    def __init__(self,filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename,self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

with openfile("sample.txt",'w') as f:
    f.write('check123')

print(f.closed)