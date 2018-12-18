import FileOperations
import datetime


class Logger:

    def __init__(self):
        pass

    def writeLog(self, directory, lines, level="info", mode="a+"):
        file = FileOperations.FileOperations.open_file(
            FileOperations.FileOperations.join(directory, level + "_log.txt"), mode)
        FileOperations.FileOperations.writeLineToFile(file, str(datetime.datetime.now()))
        for line in lines:
            FileOperations.FileOperations.writeLineToFile(file,  line)
        FileOperations.FileOperations.close_file(file)