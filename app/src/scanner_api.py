from aiohttp import web
from json import dumps
from app.src.services import is_port_open, is_valid_port, is_valid_type_data_request, compare_port
import logging
from parameters_validation import validate_parameters


logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
routes = web.RouteTableDef()


@validate_parameters
def check_ports(ip, begin: is_valid_port(int), end: is_valid_port(int)):
    lst_to_request = []
    for port in range(begin, end + 1):
        data = {}
        status = 'open' if is_port_open(ip, port) else 'close'
        data['port'] = port
        data['status'] = status
        lst_to_request.append(data)
        logging.info(f"host: {ip} port: {port} status: {status}")

    return web.Response(text=dumps(lst_to_request), status=200)


@routes.get('/scan/{ip}/{begin}/{end}')
@validate_parameters
async def get_port_status(request: is_valid_type_data_request(object)):
    """
    This handle returns status of ports
    :param request:
    :return:
    """

    logging.info('scan request received')
    ip = request.match_info['ip']
    begin = int(request.match_info['begin'])
    end = int(request.match_info['end'])

    return check_ports(ip, begin, end)


if __name__ == '__main__':
    app = web.Application()
    app.add_routes(routes)
    web.run_app(app)
