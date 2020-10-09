import os

class Remover:

    def __init__(self, directory, delete_dir=False, file_ext='.bak', parent_ext='.doc'):
        self.directory = directory
        self.delete_dir = delete_dir
        self.file_ext = file_ext
        self.parent_ext = parent_ext

    def delete_parentless_file(self):
        for root, dirs, files in os.walk(self.directory, topdown=False):
            for file in files:
                filename, file_extension = os.path.splitext(file)
                if file_extension == self.file_ext and filename + self.parent_ext not in files:
                    os.remove(os.path.join(root, file))

            if self.delete_dir:
                self.delete_empty_directory(root)

    @staticmethod
    def delete_empty_directory(directory):
        if len(os.listdir(directory)) == 0:
            os.rmdir(directory)
