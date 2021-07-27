from contextlib import contextmanager


# Content Manager as a class

class FileManager():
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, type, value, traceback):
        self.file.close()


# Content Manager as a function


@contextmanager
def file_manager(name, mode):
    f = open(name, mode)
    yield f
    f.close()


if __name__ == "__main__":
    with file_manager("test_func.txt", 'w') as f:
        f.write("Test")

    with FileManager("test_class.txt", 'w') as f:
        f.write("Test")
