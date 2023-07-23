"""Tests for count fruits function."""
from design_challenge.day1.after_tomaluuk import count_fruits
import pytest


def test_list():
    assert count_fruits(
        [
            "apple",
            "banana",
            "apple",
            "cherry",
            "banana",
            "cherry",
            "apple",
            "apple",
            "cherry",
            "banana",
            "cherry",
        ]
    ) == {"apple": 4, "banana": 3, "cherry": 4}


def test_empty_list() -> None:
    """Test an empty input list."""
    assert count_fruits([]) == {}


def test_invalid_input() -> None:
    """Test an invalid input that is not a list"""
    with pytest.raises(TypeError):
        count_fruits(3)


def test_omitted_input() -> None:
    """Test an invalid input that is not a list"""
    with pytest.raises(TypeError):
        count_fruits()
