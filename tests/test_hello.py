"""Tests for qcom_oss_pypi_pilot.hello."""

import pytest
from qcom_oss_pypi_pilot.hello import greet


def test_greet_default():
    assert greet() == "Hello, World!"


def test_greet_custom_name():
    assert greet("PyPI") == "Hello, PyPI!"


def test_greet_empty_string():
    assert greet("") == "Hello, !"


@pytest.mark.parametrize("name,expected", [
    ("Alice", "Hello, Alice!"),
    ("Bob",   "Hello, Bob!"),
    ("123",   "Hello, 123!"),
])
def test_greet_parametrized(name, expected):
    assert greet(name) == expected
