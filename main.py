from aiohttp import web
from app.src import scanner_api

app = web.Application()

if __name__ == '__main__':
    app.add_routes(scanner_api.routes)
    web.run_app(app)