# Knock Python library

Knock API access for applications written in Python.

## Documentation

See the [documentation](https://docs.knock.app) for Python usage examples.

## Installation

To install from PyPi, run the following:

```bash
pip install knock-py
```

To install from source, clone the repo and run the following:

```bash
python setup.py install
```

## Configuration

To use the library you must provide a secret API key, provided in the Knock dashboard.

```python
import knock

knock.api_key = "sk_12345"
```
