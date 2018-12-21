class Event:

    def __init__(self, headers, line):
        self.prefix = None
        # Do not use from outside directly
        self.data = {}
        self.prefix = line.split(": ")[0]
        values = line.split(": ")[1].strip().split(",")
        counter = 0
        for header in headers:
            self.data[header] = values[counter]
            counter += 1

    def get_value(self, header):
        return self.data.get(header)

    def set_value(self, header, value):
        self.data[header] = value

    def get_event(self):
        line = self.prefix + ": "
        for k, v in self.data.items():
            line += v + ","
        line = line[:-1]
        return line
