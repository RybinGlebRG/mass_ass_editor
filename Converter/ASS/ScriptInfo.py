class ScriptInfo:

    def __init__(self):
        self.lines = []

    def add_info(self, line):
        self.lines.append(line)

    def get_info_lines(self):
        return self.lines
