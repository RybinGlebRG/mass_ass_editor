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
            # print(file.number)
            srt.parse(file)
            srt_dict[file.number] = srt
        examples = FilesList.FilesList()
        examples.load(configuration.getValue("example_directory"), configuration.getValue("example_suffixes"),
                      configuration,
                      False)
        ass = None
        for example in examples:
            if example.fileName in configuration.getValue("example_name"):
                ass = ASS()
                ass.parse(example)
                break

        conversion = Conversion()
        res_asses = []
        for file in files:
            conversion.set_file(file, srt_dict[file.number], ass)
            res_ass = conversion.process()
            res_ass.name = file.fileName[:-3] + "ass"
            res_ass.directory = file.path
            res_asses.append(res_ass)
            # path = FileOperations.FileOperations.join(configuration.getValue("directory")[0], "text.txt")
            # FileOperations.FileOperations.write_lines_to_file(path, lines, "a+")
        path = FileOperations.FileOperations.join(configuration.getValue("directory")[0],
                                                  configuration.getValue("target")[0])
        FileOperations.FileOperations.makedirs(path)
        for res_ass in res_asses:
            path = FileOperations.FileOperations.join(configuration.getValue("directory")[0],
                                                      configuration.getValue("target")[0])
            path = FileOperations.FileOperations.join(path, res_ass.name)
            FileOperations.FileOperations.write_lines_to_file(path, res_ass.to_lines())
        print("The end")
