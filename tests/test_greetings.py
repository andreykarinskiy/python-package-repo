import pytest

from minipkg import greet


def test_greet_default():
    assert greet("Анна") == "Привет, Анна."


def test_greet_trim_whitespace():
    assert greet("  ") == "Привет, мир."


def test_greet_excited():
    assert greet("Python", excited=True) == "Привет, Python!"


def test_greet_type_error():
    with pytest.raises(TypeError):
        greet()  # type: ignore[call-arg]
