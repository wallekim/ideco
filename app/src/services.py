import socket


def is_port_open(host, port):
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
