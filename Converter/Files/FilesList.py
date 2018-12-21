import FileOperations
from Converter.Files import File


class FilesList:

    def __init__(self):
        self.filesList = []

    def __eq__(self, other):
        if self.filesList != other.filesList:
            return False
        return True

    def __ne__(self, other):
        if self.filesList != other.filesList:
            return True
        return False

    def __getitem__(self, key):
        return self.filesList[key]

    def __iter__(self):
        return iter(self.filesList)

    def get_list(self):
        return self.filesList

    def add(self, file):
        self.filesList.append(file)

    def filter_by_number(self, lower, upper):
        filtered = FilesList()
        lower = int(lower[0])
        upper = int(upper[0])
        for file in self.filesList:
            if lower <= file.number <= upper:
                filtered.add(file)
        return filtered

    def filter_by_suffixes(self, suffixes):
        filtered = FilesList()
        # Should not filter by suffixes if there are no suffixes
        if suffixes is None:
            return filtered
        for file in self.filesList:
            if file.getSuffix() in suffixes:
                filtered.add(file)
        return filtered

    def load(self, directories, suffixes, configuration, is_recursive=True):
        for directory in directories:
            for vector in FileOperations.FileOperations.walk(directory):
                for file in vector[2]:
                    new_file = File.File(file, vector[0])
                    if new_file.getSuffix() in suffixes:
                        new_file.check_specified(configuration)
                        self.add(new_file)
                if not is_recursive:
                    break

    def clear(self):
        self.filesList.clear()
