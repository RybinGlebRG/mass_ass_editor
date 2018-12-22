class Event:

    def __init__(self):
        self.number = None
        self.start = None
        self.end = None
        self.text = []

    def get_normalized_start(self, suffix="ASS"):
        result = self.start
        if suffix == "ASS":
            result = result.lstrip("0")
            if result[0] == ":":
                result = "0" + result
            n = result.find(",")
            if len(result) - 1 > n+2:
                result = result[:n + 3]
            result = result.replace(",", ".")
            return result

    def get_normalized_end(self, suffix="ASS"):
        result = self.end
        if suffix == "ASS":
            result = result.lstrip("0")
            if result[0] == ":":
                result = "0" + result
            n = result.find(",")
            if len(result) - 1 - n > 2:
                result = result[:n + 2]
            result = result.replace(",", ".")
            return result
