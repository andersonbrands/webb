def task(func):
    func.create_doit_tasks = func
    return func


DOIT_CONFIG = {
    "default_tasks": ["_list"],
    "verbosity": 2,
    "backend": "json",
}


@task
def _list():
    return dict(actions=["doit list"])


def actions(*cmds):
    return task(lambda: dict(actions=cmds))


requirements_dev = actions('pip-compile -o requirements-dev.txt requirements/dev.in')
