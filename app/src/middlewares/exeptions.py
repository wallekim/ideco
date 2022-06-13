class MiddlewaresError(Exception):
    pass


class IncorrectTypesForPorts(MiddlewaresError):
    """Exception raised for errors in the input type ports."""
    def __init__(self, begin, end, message='Port value is not valid'):
        self.begin = begin
        self.end = end
        self.message = message


class PortMustBeMoreThanZero(IncorrectTypesForPorts):
    """Exception raised for errors in the input value of port."""

    def __init__(self, port, message='Port value is less than zero'):
        self.port = port
        self.message = message
