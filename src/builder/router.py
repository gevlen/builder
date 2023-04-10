from pathlib import Path

from fastapi import APIRouter
from fastapi.responses import ORJSONResponse

from src.builder.controller import get_file
from src.builder.schema import BuildNameIn
from src.builder.schema import BuildNode
from src.builder.schema import TaskNode
from src.builder.schema import ErrorOut
from src.builder.interactor import get_tasks
from src.builder.interactor import get_build_tasks


builder_router = APIRouter(tags=["build"], prefix="/builder")

tasks = get_file(path_to_file=Path("builds", "tasks.yaml"), schema=TaskNode)
builds = get_file(path_to_file=Path("builds", "build.yaml"), schema=BuildNode)


@builder_router.post(
    path="/get_tasks", responses={200: {"model": list[str]}, 404: {"model": ErrorOut}}
)
async def retrieve_tasks(build_name: BuildNameIn):
    build_tasks = get_build_tasks(build_name=build_name.build, builds=builds)
    if not build_tasks:
        return ORJSONResponse(
            status_code=404,
            content={"detail": f"no build with name: {build_name.build}"},
        )
    return ORJSONResponse(content=get_tasks(build_tasks=build_tasks, tasks=tasks))
