from Converter.SRT.Event import Event
import FileOperations


# TODO: Write tests for this class
class SRT:

    def __init__(self):
        self.events = {}

    def parse(self, file):
        name = FileOperations.FileOperations.join(file.path, file.fileName)
        lines = FileOperations.FileOperations.readFile(name,"cp1251")
        is_number_next = True
        is_time_next = False
        is_text_next = False
        current_number = 0
        for line in lines:
            #print(repr(line))
            line = line.strip()
            if len(line) == 0:
                is_number_next = True
                is_time_next = False
                is_text_next = False
                continue
            if is_number_next:
                number = int(line)
                current_number = number
                event = Event()
                event.number = number
                self.events[number] = event
                is_number_next = False
                is_time_next = True
                continue
            if is_time_next:
                timings = line.split(" --> ")
                self.events[current_number].start = timings[0]
                self.events[current_number].end = timings[1]
                is_time_next = False
                is_text_next = True
                continue
            if is_text_next:
                self.events[current_number].text.append(line)
                continue
