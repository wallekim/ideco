from aiohttp import web
from app.src import scanner_api
from app.src.middlewares.error_middleware import error_handler

app = web.Application()

if __name__ == '__main__':
    app.middlewares.append(error_handler)
    app.add_routes(scanner_api.routes)
    web.run_app(app)