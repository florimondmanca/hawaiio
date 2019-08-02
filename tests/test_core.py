import time

import pytest

from hawaiio import run, sleep


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


@pytest.mark.parametrize("seconds", (0.001, 0.01, 0.1, 1))
def test_sleep(seconds: float):
    async def sleepy():
        await sleep(seconds)
        return "Hello"

    t = time.time()
    assert run(sleepy()) == "Hello"
    assert pytest.approx(time.time() - t, 0.1) == seconds


def test_sleep_must_be_positive():
    async def bad_sleep():
        await sleep(-1)

    with pytest.raises(ValueError):
        run(bad_sleep())
