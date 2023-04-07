# Contributing

## Getting Started

1. Install [asdf](https://asdf-vm.com)
2. Install the asdf Python plugin

```bash
asdf plugin add python https://github.com/danhper/asdf-python.git # Visit that repository to see installation prerequisites
```

3. Run `asdf install` to install the version of Python specified in the [.tool-versions](.tool-versions) file
4. Run `pip install -r requirements.txt` to install the Python dependencies

## Running the tests

```bash
python -m pytest
```

## Running the linter

```bash
flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
```
