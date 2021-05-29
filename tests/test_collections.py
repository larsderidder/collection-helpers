from collection_utils import (
    compact,
    ensure_list,
    flatten,
    maybe_float,
    maybe_int,
    remove_empties_from_dict,
)


def test_remove_empties():
    data = {"a": 1, "b": None, "c": {"d": None, "e": 2}}
    cleaned = remove_empties_from_dict(data)
    assert cleaned == {"a": 1, "c": {"e": 2}}


def test_ensure_list():
    assert ensure_list(1) == [1]
    assert ensure_list([1, 2]) == [1, 2]


def test_maybe_int_and_float():
    assert maybe_int("3") == 3
    assert maybe_int("nope") is None
    assert maybe_float("3.5") == 3.5
    assert maybe_float(None) is None


def test_compact_and_flatten():
    assert compact([1, None, 2]) == [1, 2]
    assert flatten([[1, 2], (3, 4), 5]) == [1, 2, 3, 4, 5]
