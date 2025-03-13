from mytime import Time


class TimeWithSeconds(Time):
    def __init__(self, hour, minute, second):
        super().__init__(hour, minute)
        self.second = second

    def __str__(self):
        return super().__str__() + f":{self.second:02}"
