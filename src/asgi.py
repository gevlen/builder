from fastapi import FastAPI

from src.builder.router import builder_router


def create_app() -> FastAPI:
    api = FastAPI(
        title="Builds-Service",
        debug=False,
    )
    api.include_router(builder_router)
    return api


app = create_app()


@app.get("/ping/")
async def root() -> str:
    return "pong"
