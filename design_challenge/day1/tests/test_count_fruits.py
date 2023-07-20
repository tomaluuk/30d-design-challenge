"""Tests for count fruits function."""
from design_challenge.day1.after_tomaluuk import count_fruits


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
    assert count_fruits(fruits=[]) == {}