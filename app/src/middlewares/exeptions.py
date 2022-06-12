class MiddlewaresError(Exception):
    pass


class IncorrectTypesForPorts(MiddlewaresError):
    pass


class PortMustBeMoreThanZero(IncorrectTypesForPorts):
    pass


class BeginPortGreaterEnd(IncorrectTypesForPorts):
    pass
