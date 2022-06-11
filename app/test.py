from aiohttp.test_utils import AioHTTPTestCase
from aiohttp import web
from src.scanner_api import handle


class MyAppTestCase(AioHTTPTestCase):

    async def get_application(self):
        app = web.Application()
        app.router.add_get('/scan/{ip}/{begin}/{end}', handle)
        return app

    async def test_get(self):
        async with self.client.request("GET", "/scan/localhost/1/2") as resp:
            self.assertEqual(resp.status, 200)
            text = await resp.text()
        self.assertIn('[{"port": 1, "status": "close"}, {"port": 2, "status": "close"}]', text)

