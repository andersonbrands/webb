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


@_task
def requirements_compile():
    dev = dict(
        in_files=["requirements/dev.in", "requirements/prod.in"],
        out_file="requirements-dev.txt",
        name="dev",
    )
    prod = dict(
        in_files=["requirements/prod.in"],
        out_file="requirements-prod.txt",
        name="prod",
    )
    for env in [dev, prod]:
        out = env["out_file"]
        ins = " ".join(env["in_files"])
        name = env["name"]

        yield task(
            f"pip-compile -o {out} {ins}",
            name=name,
        )()


requirements_dev_install = task(
    "pip install -r requirements-dev.txt",
)

requirements_prod_install = task(
    "pip install -r requirements-prod.txt",
)
