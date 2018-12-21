from Converter.ASS import Event


class Events:

    def __init__(self):
        self.headers = None
        self.events = []

    def add_headers(self, line):
        values = line.split(":")[1].strip().split(", ")
        self.headers = values

    def add_event(self, line):
        event = Event.Event(self.headers, line)
        self.events.append(event)

    def get_events(self):
        lines = []
        line = "Format: "
        for header in self.headers:
            line += header + ", "
        line = line[:-2]
        lines.append(line)
        for event in self.events:
            line = event.get_event()
            lines.append(line)
        return lines

    def get_example_event(self):
        return self.events[0]
