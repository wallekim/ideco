from aiohttp import web
from json import dumps
from .services import is_port_open
import logging

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
routes = web.RouteTableDef()


@routes.get('/scan/{ip}/{begin}/{end}')
async def handle(request):
    logging.info('scan request received')
    ip = request.match_info['ip']
    begin = int(request.match_info['begin'])
    end = int(request.match_info['end'])
    lst_to_request = []
    for port in range(begin, end + 1):
        data = {}
        status = 'open' if is_port_open(ip, port) else 'close'
        data['port'] = port
        data['status'] = status
        lst_to_request.append(data)
        logging.info(f"host: {ip} port: {port} status: {status}")

    return web.Response(text=dumps(lst_to_request), status=200)


if __name__ == '__main__':
    app = web.Application()
    app.add_routes(routes)
    web.run_app(app)
