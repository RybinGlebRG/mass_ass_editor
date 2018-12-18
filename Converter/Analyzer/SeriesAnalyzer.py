import re
from Converter.Analyzer import AnalyzingGroup

class SeriesAnalyzer:

    def __init__(self):
        pass

    @staticmethod
    def findHypoteses(files):
        for file in files:
            file.possibleSeriesNumbers = re.findall("\d+", file.fileName)
            for i in range(0, len(file.possibleSeriesNumbers)):
                file.possibleSeriesNumbers[i] = file.possibleSeriesNumbers[i].lstrip("0")
                if file.possibleSeriesNumbers[i] == "":
                    file.possibleSeriesNumbers[i] = 0
                else:
                    file.possibleSeriesNumbers[i] = int(file.possibleSeriesNumbers[i])

    @staticmethod
    def getGroupIdByPath(analyzingGroupsList, path):
        for i in range(0, len(analyzingGroupsList)):
            if analyzingGroupsList[i].path == path:
                return i

    # Разбиваем общий список на подсписки на основе каталога расположения
    @staticmethod
    def divideByGroup(files):
        appended = []
        analyzingGroupsList = []
        for file in files:
            if file.path not in appended:
                appended.append(file.path)
                analyzingGroupsList.append(AnalyzingGroup.AnalyzingGroup(file.path))
                analyzingGroupsList[
                    SeriesAnalyzer.getGroupIdByPath(analyzingGroupsList, file.path)].files.append(file)
            else:
                analyzingGroupsList[
                    SeriesAnalyzer.getGroupIdByPath(analyzingGroupsList, file.path)].files.append(file)
        return analyzingGroupsList

    @staticmethod
    def checkConditionsForGroup(group, currentHypothesis):
        isGrowing = True
        hypoteses = []
        for file in group.files:
            if file.number is not None:
                hypoteses.append(file.number)
            else:
                hypoteses.append(file.possibleSeriesNumbers[currentHypothesis])
        hypoteses.sort()

        for i in range(1, len(hypoteses)):
            previous = hypoteses[i - 1]
            current = hypoteses[i]

            if current <= previous:
                isGrowing = False

        if isGrowing:
            return True
        else:
            return False

    @staticmethod
    def analyzeHypoteses(files, groups):
        currentHypothesis = None
        for group in groups:
            # Полагаем, что в группе файлов все файлы, которые отличаются только номером серии
            # имеют номер серии, равный None. Файлы, отличающиеся от основных должны быть явно
            # прописаны в пользовательской конфигурации и на данный момент уже иметь номер серии
            length = None
            for file in group.files:
                if file.number is None:
                    length = len(file.possibleSeriesNumbers)
                    break
            for i in range(0, length):
                currentHypothesis = i
                conditionsMet = SeriesAnalyzer.checkConditionsForGroup(group, currentHypothesis)
                if conditionsMet:
                    group.hypothesis = currentHypothesis
                    break

    @staticmethod
    def setFileNumber(files):
        SeriesAnalyzer.findHypoteses(files)

        groups = SeriesAnalyzer.divideByGroup(files)
        SeriesAnalyzer.analyzeHypoteses(files, groups)

        for group in groups:
            for file in group.files:
                if file.number is None:
                    file.number = file.possibleSeriesNumbers[group.hypothesis]