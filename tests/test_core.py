import time

import pytest

import hawaiio
import hawaiio.testing


async def noop():
    pass


async def greet(name: str):
    return f"Hello, {name}"


@pytest.mark.parametrize(
    "func, args, result",
    [(noop, (), None), (greet, ("world",), "Hello, world")],
)
def test_run(func, args, result):
    assert hawaiio.run(func(*args)) == result


async def sleepy(seconds):
    await hawaiio.sleep(seconds)
    return "Hello"


@pytest.mark.parametrize("seconds", (0, 0.001, 0.01, 0.1, 1))
def test_sleep(seconds: float):
    t = time.time()
    assert hawaiio.run(sleepy(seconds)) == "Hello"
    if not seconds:
        assert time.time() - t < 1e-4
    else:
        assert pytest.approx(time.time() - t, 0.1) == seconds


def test_sleep_must_be_positive():
    async def bad_sleep():
        await hawaiio.sleep(-1)

    with pytest.raises(ValueError):
        hawaiio.run(bad_sleep())


def test_clock_outside_context():
    with pytest.raises(RuntimeError):
        hawaiio.time()


def test_sleep_custom_clock():
    clock = hawaiio.testing.MockClock()
    assert hawaiio.run(sleepy(1), clock=clock) == "Hello"
    assert clock.time() == clock.ticks == 1
