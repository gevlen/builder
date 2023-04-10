from __future__ import annotations

from pydantic import BaseModel


class BuildNameIn(BaseModel):
    build: str


class BuildModel(BaseModel):
    name: str
    tasks: list[str]


class BuildNode(BaseModel):
    builds: list[BuildModel]


class TaskModel(BaseModel):
    name: str
    dependencies: list[str]


class TaskNode(BaseModel):
    tasks: list[TaskModel]


class ErrorOut(BaseModel):
    detail: str
