from typing import Callable


def _task(func: Callable):
    func.create_doit_tasks = func
    return func


DOIT_CONFIG = {
    "default_tasks": ["_list"],
    "verbosity": 2,
    "backend": "json",
}


def task(*cmds, file_dep=None, targets=None, task_dep=None, **kwargs):
    return _task(
        lambda: dict(
            actions=cmds,
            file_dep=file_dep or [],
            targets=targets or [],
            task_dep=task_dep or [],
            **kwargs,
        )
    )


_list = task("doit list")


requirements_dev_compile = task(
    "pip-compile -o requirements-dev.txt requirements/dev.in",
    file_dep=["requirements/dev.in"],
    targets=["requirements-dev.txt"],
)

requirements_dev_install = task(
    "pip install -r requirements-dev.txt",
)
