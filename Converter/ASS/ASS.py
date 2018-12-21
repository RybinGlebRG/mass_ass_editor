import FileOperations
from Converter.ASS import ScriptInfo
from Converter.ASS import V4Styles
from Converter.ASS import Events


class ASS:

    def __init__(self):
        self.script_info = None
        self.v4_styles = None
        self.events = None
        self.example_event = None

    def parse(self, file):
        name = FileOperations.FileOperations.join(file.path, file.fileName)
        lines = FileOperations.FileOperations.readFile(name)
        is_script_info = True
        is_v4_styles = False
        is_events = False
        self.script_info = ScriptInfo.ScriptInfo()
        self.v4_styles = V4Styles.V4Styles()
        self.events = Events.Events()
        is_header_next = False
        for line in lines:
            line = line.strip()
            if len(line) == 0:
                if is_script_info:
                    is_script_info = False
                    is_v4_styles = True
                    continue
                if is_v4_styles:
                    is_v4_styles = False
                    is_events = True
                    continue
                continue
            if is_script_info:
                if line == "[Script Info]":
                    continue
                self.script_info.add_info(line)
                continue
            if is_v4_styles:
                if line == "[V4+ Styles]":
                    continue
                self.v4_styles.add_info(line)
                continue
            if is_events:
                if line == "[Events]":
                    is_header_next = True
                    continue
                if is_header_next:
                    self.events.add_headers(line)
                    is_header_next = False
                    continue
                self.events.add_event(line)
                continue

    def get_script_info(self):
        lines = self.script_info.get_info_lines()
        return lines

    def get_v4_styles(self):
        lines = self.v4_styles.get_v4_styles()
        return lines

    def get_events(self):
        lines = self.events.get_events()
        return lines

    def replace_as_in_example_event(self, header, value):
        self.example_event = self.events.get_example_event()
        self.example_event.set_value(header, value)

    def get_replaced_example_event(self):
        line = self.example_event.get_event()
        return line
