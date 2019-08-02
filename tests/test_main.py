import pytest

from hawaiio import run


async def noop():
    pass


async def greet(name: str):
    return f"Hello, {name}"


@pytest.mark.parametrize(
    "func, args, result",
    [(noop, (), None), (greet, ("world",), "Hello, world")],
)
def test_run(func, args, result):
    assert run(func(*args)) == result
