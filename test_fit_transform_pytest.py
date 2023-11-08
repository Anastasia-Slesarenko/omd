from one_hot_encoder import fit_transform
import pytest


def test_hello_world():
    actual = fit_transform(["Hello", "world", "Hello"])
    expected = [
        ("Hello", [0, 1]),
        ("world", [1, 0]),
        ("Hello", [0, 1])
     ]
    assert actual == expected


def test_empty_string():
    actual = fit_transform('')
    expected = [("", [1])]
    assert actual == expected


def test_not_iterable():
    with pytest.raises(TypeError) as context:
        fit_transform(123)
    assert "'int' object is not iterable" == str(context.value)


def test_without_arguments():
    with pytest.raises(TypeError) as context:
        fit_transform()
    assert"expected at least 1 arguments, got 0" == str(context.value)


if __name__ == "__main__":
    pass
