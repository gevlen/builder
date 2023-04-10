from collections import deque

from src.builder.schema import TaskNode
from src.builder.schema import BuildNode


class Parser:
    def __init__(self, tasks: dict[str, list[str]]):
        self.tasks = tasks
        self.stack: deque[str] = deque()
        self.result: list[str] = []
        self.unique_tasks: set[str] = set()

    def parse(self, tasks) -> None:
        for task in tasks:
            self._parse_task(task)

    def _parse_task(self, task_in: str) -> None:
        if not self.tasks[task_in]:
            self._append_to_result(task_in)
            return
        else:
            self.stack.append(task_in)
            for task in self.tasks[task_in]:
                self._parse_task(task)
            self._append_to_result(self.stack.pop())

    def _append_to_result(self, task: str):
        if task not in self.unique_tasks:
            self.result.append(task)
            self.unique_tasks.add(task)


def _convert_tasks_to_dict(tasks: TaskNode) -> dict[str, list[str]]:
    converted_tasks = {}
    for task in tasks.tasks:
        converted_tasks.update({task.name: task.dependencies})
    return converted_tasks


def get_build_tasks(build_name: str, builds: BuildNode) -> list[str] | None:
    for build in builds.builds:
        if build.name == build_name:
            return build.tasks
    return None


def get_tasks(build_tasks: list[str], tasks: TaskNode) -> list[str]:
    converted_tasks = _convert_tasks_to_dict(tasks)
    parser = Parser(converted_tasks)
    parser.parse(build_tasks)
    return parser.result
