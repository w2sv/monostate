# __monostate__
Dependency-free python package, providing monostate owner base class through implementation of the borg pattern

[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)
[![Build](https://github.com/w2sv/monostate/actions/workflows/build.yaml/badge.svg)](https://github.com/w2sv/monostate/actions/workflows/build.yaml)
[![codecov](https://codecov.io/gh/w2sv/monostate/branch/master/graph/badge.svg?token=9EESND69PG)](https://codecov.io/gh/w2sv/monostate)
![PyPI](https://img.shields.io/pypi/v/monostate)
[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/tterb/atomic-design-ui/blob/master/LICENSEs)

## Download
```
pip install monostate
```

## Usage

```python
from monostate import MonoStateOwner


class MonoStateOwnerImplementation(MonoStateOwner):
    def __init__(self, a, b):
        super().__init__()
        
        # initialize instance as per usual...
        
        
# Initialization of state:
MonoStateOwnerImplementation(69, 420)

# Instance retrieving:
instance = MonoStateOwnerImplementation.instance()
```

- Managing of multiple MonoStateOwner Subclasses with decoupled states supported

## Author
Janek Zangenberg

## License
[MIT](LICENSE)
