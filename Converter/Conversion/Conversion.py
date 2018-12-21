class Conversion:

    def __init__(self):
        self.file = None
        self.srt = None
        self.ass = None
        self.example = None

    def set_file(self, file, srt, example):
        self.file = file
        self.srt = srt
        self.example = example

    def process(self):
        lines = []
        script_info = self.example.get_script_info()
        v4_styles = self.example.get_v4_styles()
        events_headers = self.example.get_events()[0]
        ass_events = []
        for event in self.srt.events.values():
            self.example.replace_as_in_example_event("Start", event.start.replace(",", "."))
            self.example.replace_as_in_example_event("End", event.end.replace(",", "."))
            res_line = ""
            for line in event.text:
                res_line += line + "\\N"
            res_line = res_line[:-2]
            self.example.replace_as_in_example_event("Text", res_line)
            res_event = self.example.get_replaced_example_event()
            ass_events.append(res_event)
        lines.append("[Script Info]")
        for line in script_info:
            lines.append(line)
        lines.append("")
        lines.append("[V4+ Styles]")
        for line in v4_styles:
            lines.append(line)
        lines.append("")
        lines.append("[Events]")
        lines.append(events_headers)
        for line in ass_events:
            lines.append(line)
        return lines
