import typing


def run(coro: typing.Coroutine[None, None, typing.T]) -> typing.T:
    try:
        coro.send(None)
    except StopIteration as exc:
        return exc.value
