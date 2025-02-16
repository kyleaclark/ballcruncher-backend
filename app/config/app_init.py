import logging

from fastapi.applications import FastAPI

from app.api.api_router import api_router

logger = logging.getLogger(__name__)


def create_app() -> FastAPI:
    logger.info("Begin creating fastapi app new instance")

    result = FastAPI()
    result.include_router(api_router, prefix="")

    return result
