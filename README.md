# hawaiio

[![build status](https://travis-ci.com/florimondmanca/hawaiio.svg?branch=master)](https://travis-ci.com/florimondmanca/hawaiio)
[![codecov](https://codecov.io/gh/florimondmanca/hawaiio/branch/master/graph/badge.svg)](https://codecov.io/gh/florimondmanca/hawaiio)
[![code style](https://img.shields.io/badge/code_style-black-black)](https://github.com/psf/black)
![license](https://img.shields.io/badge/license-MIT-green)

**hawaiio** is an experimental library of building blocks for concurrent Python programs. It relies on the async/await syntax, and nothing more.

## Installation

```
pip install hawaiio
```

## Usage

```python
from hawaiio import run, sleep

async def greet(name: str):
    await sleep(1)
    return f"Hello, {name}"

message = run(greet("world"))
print(message)  # 'Hello, world'
```

## Changelog

See [CHANGELOG.md](https://github.com/florimondmanca/hawaiio/tree/master/CHANGELOG.md).

## Contributing

See [Contributing guidelines](https://github.com/florimondmanca/hawaiio/tree/master/CONTRIBUTING.md).

## License

MIT
