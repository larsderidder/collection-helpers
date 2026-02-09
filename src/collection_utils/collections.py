"""Small collection helpers."""

from __future__ import annotations

from typing import Any, Iterable, List, Optional


def remove_empties_from_dict(a_dict: dict) -> dict | None:
    """Remove keys with value None, recursively."""
    result: dict = {}
    for key, value in a_dict.items():
        if isinstance(value, dict):
            value = remove_empties_from_dict(value)
        if isinstance(value, list):
            keep: list = []
            for item in value:
                if isinstance(item, dict):
                    keep.append(remove_empties_from_dict(item))
                elif item is not None:
                    keep.append(item)
            value = keep
        if value is not None:
            result[key] = value
    return result or None


def _wrap_single(value: Any) -> list[Any]:
    """Wrap a scalar value in a list."""
    return [value]


def ensure_iterable(maybe_iterable: Any) -> Iterable[Any]:
    """Make sure the input is iterable."""
    try:
        iter(maybe_iterable)
    except TypeError:
        return _wrap_single(maybe_iterable)
    return maybe_iterable  # type: ignore[return-value]


def ensure_list(maybe_list: Any) -> List[Any]:
    """Make sure the input is a list."""
    return maybe_list if isinstance(maybe_list, list) else _wrap_single(maybe_list)


def compact(values: Iterable[Any]) -> list[Any]:
    """Return a list with all None values removed."""
    return [value for value in values if value is not None]


def flatten(items: Iterable[Any]) -> list[Any]:
    """Flatten one level of nested iterables (list/tuple/set)."""
    flat: list[Any] = []
    for item in items:
        if isinstance(item, (list, tuple, set)):
            flat.extend(item)
        else:
            flat.append(item)
    return flat


def set_if_not_none(obj: object, field: str, value: Optional[Any], overwrite: bool = False) -> None:
    """Set the value if it is not None."""
    if value is not None:
        if overwrite or getattr(obj, field) in (None, ""):
            setattr(obj, field, value)


def maybe_int(value: Any) -> int | None:
    try:
        return int(value)
    except (ValueError, TypeError):
        return None


def maybe_float(value: Any) -> float | None:
    try:
        return float(value)
    except (ValueError, TypeError):
        return None
