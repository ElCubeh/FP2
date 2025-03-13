class TimeError(Exception):
    pass


class HourError(TimeError):
    def __init__(self, value_error, message=""):
        super().__init__(message)
        self.value_error = value_error


class MinuteError(TimeError):
    def __init__(self, value_error, message=""):
        super().__init__(message)
        self.value_error = value_error
