import time
import types
import typing

__all__ = ("run", "sleep")


def run(coro: typing.Coroutine[None, None, typing.T]) -> typing.T:
    while True:
        try:
            coro.send(None)
        except StopIteration as exc:
            return exc.value


@types.coroutine
def sleep(seconds: float):
    if seconds < 0:
        raise ValueError(f"'seconds' must be positive (got {seconds})")
    start = time.time()
    while time.time() - start < seconds:
        yield
