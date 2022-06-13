from parameters_validation import parameter_validation
from app.src.middlewares.exeptions import IncorrectTypesForPorts, PortMustBeMoreThanZero, BeginPortGreaterEnd
import socket


def is_port_open(host: str, port: int):
    """
    This function is using to check opened ports of remote host
    :param host: name of host (str)
    :param port: (int)
    :return: boolean True if port is opened
    """
    s = socket.socket()
    try:
        s.connect((host, port))
        s.settimeout(0.2)
    except:
        return False
    else:
        return True
    finally:
        s.close()


@parameter_validation
def is_valid_port(port: int):
    """
    Validator raises exception if port number < 0
    :param port: (int)
    """
    if port < 0:
        raise PortMustBeMoreThanZero(port)


@parameter_validation
def is_valid_type_data_request(request):
    """
    Validator raises exception if begin or end port are not integer
    :param request: input request object
    """
    begin = request.match_info['begin']
    end = request.match_info['end']
    try:
        begin = int(begin)
        end = int(end)
    except:
        raise IncorrectTypesForPorts(begin, end)
    else:
        if begin > end:
            raise BeginPortGreaterEnd(begin, end)
