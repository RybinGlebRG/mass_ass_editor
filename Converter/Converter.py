from Converter.Configuration import Configuration
from Converter.Files import FilesList
from Converter.Analyzer import SeriesAnalyzer


class Converter:

    def __init__(self):
        pass

    def convert(self, directory, configuration_file):
        configuration = Configuration.Configuration()
        configuration.fill(configuration_file)
        files = FilesList.FilesList()
        files.load([directory], configuration.getValue("suffixes"), configuration, False)
        SeriesAnalyzer.SeriesAnalyzer.setFileNumber(files)
        

