from aiohttp.test_utils import AioHTTPTestCase
from aiohttp import web
from app.src.scanner_api import get_port_status
from app.src.middlewares.exeptions import IncorrectTypesForPorts, PortMustBeMoreThanZero


class MyAppTestCase(AioHTTPTestCase):

    async def get_application(self):
        app = web.Application()
        app.router.add_get('/scan/{ip}/{begin}/{end}', get_port_status)
        return app

    async def test_get(self):
        async with self.client.request("GET", "/scan/localhost/1/2") as resp:
            self.assertEqual(resp.status, 200)
            text = await resp.text()
        self.assertIn('[{"port": 1, "status": "close"}, {"port": 2, "status": "close"}]', text)

    async def test_validation_input_data(self):
        async with self.client.request("GET", "/scan/localhost/asdf/safdgd"):
            self.assertRaises(IncorrectTypesForPorts)

    async def test_validation_begin_greater_end(self):
        async with self.client.request("GET", "/scan/localhost/-100/10000"):
            self.assertRaises(PortMustBeMoreThanZero)


