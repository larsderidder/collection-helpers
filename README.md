# collection-helpers

Small helpers for lists, dicts, and safe conversions.

## Install

Install from source:

```bash
git clone https://github.com/larsderidder/collection-helpers.git
cd collection-helpers
python -m venv .venv
. .venv/bin/activate
python -m pip install -U pip
python -m pip install .
```

## Usage

```python
from collection_utils import compact, flatten, maybe_int, remove_empties_from_dict

clean = remove_empties_from_dict({"a": 1, "b": None})
value = maybe_int("42")
flat = flatten([[1, 2], (3, 4), 5])
values = compact([1, None, 2])
```

## Development

```bash
python -m venv .venv
. .venv/bin/activate
python -m pip install -U pip
python -m pip install -e ".[dev]"
pytest
```
