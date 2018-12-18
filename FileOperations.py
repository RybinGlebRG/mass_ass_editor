import io
import os
import shutil


class FileOperations:


    @staticmethod
    def rename(oldName, newName):
        os.rename(oldName, newName)

    @staticmethod
    def walk(directory):
        lst = []
        for root, dirs, files in os.walk(directory):
            lst.append([root, dirs, files])
        return lst

    @staticmethod
    def makedirs(directory):
        os.makedirs(directory)

    @staticmethod
    def join(path1, path2):
        return os.path.join(path1, path2)

    @staticmethod
    def exists(path):
        return os.path.exists(path)

    @staticmethod
    def isfile(path):
        return os.path.isfile(path)

    @staticmethod
    def listdir(path):
        lst = []
        files = os.listdir(path)
        for file in files:
            lst.append(file)
        return lst

    @staticmethod
    def dirname(path):
        return os.path.dirname(path)

    @staticmethod
    def abspath(path):
        return os.path.abspath(path)

    @staticmethod
    def readFile(path):
        lines = []
        file = FileOperations.open_file(path)
        for line in file:
            lines.append(line)

        return lines

    @staticmethod
    def writeLineToFile(file, line):
        file.write(line + "\n")

    @staticmethod
    def open_file(path, mode="a+"):
        file = io.open(path, mode=mode, newline="\r\n", encoding="utf-8", errors="surrogateescape")
        return file

    @staticmethod
    def close_file(file):
        file.close()