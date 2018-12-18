from Converter.Configuration.Parser import Parser
import datetime


class Configuration:

    def __init__(self):
        self.keyValueList = {}

    def __eq__(self, other):
        if self.keyValueList != other.keyValueList:
            return False
        return True

    def __ne__(self, other):
        if self.keyValueList != other.keyValueList:
            return True
        return False

    def setValue(self, key, value):
        if value is None:
            self.keyValueList[key.upper()] = None
            return
        for item in value:
            if item is not None:
                break
            self.keyValueList[key.upper()] = None
            return
        self.keyValueList[key.upper()] = value

    def is_key_exists(self, key):
        if self.keyValueList.get(key.upper()) is not None:
            return True
        return False

    def fill(self, fileName):
        parser = Parser.Parser()
        dictionary = parser.parse(fileName)
        self.merge(dictionary)

    def merge(self, dictionary):
        for key, value in dictionary.items():
            self.keyValueList[key] = value

    def getValue(self, key):
        return self.keyValueList.get(key.upper())

    def isIncludes(self, key, testValue):
        value = self.getValue(key)
        if value is None:
            return False
        if testValue in value:
            return True
        return False

    def is_ready(self):
        if self.getValue("userConfigurationFile") is not None:
            return True
        return False


    def getAllPairs(self):
        return self.keyValueList.items()


    def log(self):
        lines = []
        lines.append("configurationMain:")
        items = self.getAllPairs()
        for key, value in items:
            lines.append(key + "=" + str(value))
        lines.append("-----------------------------------")
        return lines

    def print(self):
        print("-----------------------------------")
        print(datetime.datetime.now())
        print("-----------------------------------")
        print("Configuration:")
        items = self.getAllPairs()
        for key, value in items:
            print(key + "=" + str(value))
        print("-----------------------------------")


    def load(self, absolute_file_name):
        # Fill with base configuration
        self.fill(absolute_file_name)