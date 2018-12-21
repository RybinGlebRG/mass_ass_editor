from Converter.Configuration import Configuration
from Converter.Files import FilesList
from Converter.Analyzer import SeriesAnalyzer
from Converter.SRT.SRT import SRT
from Converter.ASS.ASS import ASS
from Converter.Conversion.Conversion import Conversion
import FileOperations


class Converter:

    def __init__(self):
        pass

    def convert(self, configuration_file):
        configuration = Configuration.Configuration()
        configuration.fill(configuration_file)
        files = FilesList.FilesList()
        files.load(configuration.getValue("directory"), configuration.getValue("suffixes"), configuration, False)
        SeriesAnalyzer.SeriesAnalyzer.setFileNumber(files)
        files = files.filter_by_number(configuration.getValue("first"), configuration.getValue("last"))
        srt_dict = {}
        for file in files:
            srt = SRT()
            #print(file.number)
            srt.parse(file)
            srt_dict[file.number] = srt
        examples = FilesList.FilesList()
        examples.load(configuration.getValue("directory"), configuration.getValue("example_suffixes"), configuration,
                      False)
        ass = None
        for example in examples:
            ass = ASS()
            ass.parse(example)
            break

        conversion = Conversion()
        for file in files:
            conversion.set_file(file, srt_dict[file.number], ass)
            lines = conversion.process()
            path = FileOperations.FileOperations.join(configuration.getValue("directory")[0], "text.txt")
            FileOperations.FileOperations.write_lines_to_file(path, lines,"a+")
        print("The end")