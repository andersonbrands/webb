from aiohttp import web

_CLIENT_MAX_SIZE = (1024**2) * 100


route = web.RouteTableDef()


@route.get("/greeting")
async def home(req: web.Request):
    name = req.query.get("name", "world")
    return web.Response(text=f"Hello, {name}!")


def get_web_app(cleanup_ctx_list=None):
    if cleanup_ctx_list is None:
        cleanup_ctx_list = []

    app = web.Application(client_max_size=_CLIENT_MAX_SIZE)

    app.cleanup_ctx.extend(cleanup_ctx_list)

    app.router.add_routes(route)

    return app
