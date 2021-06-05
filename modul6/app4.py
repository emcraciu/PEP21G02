class MyFile:
    def __enter__(self):
        """this method will be executed automatically when context is started"""
        self.file = open('python.text', 'a')
        return self

    def read_python_code(self):
        indent = 0
        line = input('>>> ')
        self.file.write(line + "\n")  # we write the first line to file
        if line.endswith(':'):
            indent += 1
        while line != '' or indent:

            if indent == 0:
                line = input('>>> ')
            else:
                line = input(f'... {" " * 4 * indent}')

            self.file.write(f'{" " * 4 * indent}line\n')  # we write the lines from input to file

            if line == '':
                if indent > 0:
                    indent -= 1
            elif line.endswith(':'):
                indent += 1

    def __exit__(self, exc_type, exc_val, exc_tb):
        """this method is executed automatically when context ends"""
        if exc_tb:  # exc_tb will be None if no exception occurred during execution
            self.file.write(str(exc_tb.tb_frame))
        self.file.close()
        return True  # when this method returns true any exception encountered in the context is ignored


if __name__ == '__main__':
    with MyFile() as my_file:
        my_file.read_python_code()
        my_file.read_python_code()
