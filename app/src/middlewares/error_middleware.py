from app.src.middlewares.exeptions import IncorrectTypesForPorts, PortMustBeMoreThanZero
from aiohttp.web import middleware
from aiohttp import web


def get_error_body(error) -> dict:
    """
    Returns error type and message by dict to handler
    :param error: Exception
    """
    return {"error_type": str(type(error)), "error_message": str(error.message)}


@middleware
async def error_handler(request, handler):
    """
    This function returns error type and message by json
    :param request
    :param handler
    """
    try:
        resp = await handler(request)
    except PortMustBeMoreThanZero as error:
        return web.json_response(get_error_body(error), status=500)
    except IncorrectTypesForPorts as error:
        return web.json_response(get_error_body(error), status=500)

    return resp
