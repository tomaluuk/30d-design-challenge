"""A module for day 1 submission: using the KISS principle."""


def count_fruits(fruits: list[str]) -> dict[str, int]:
    """Count the number of unique fruits in the input list `fruits`."""

    if len(fruits) == 0:
        return {}

    dict_counts = {fruit: fruits.count(fruit) for fruit in fruits}

    return dict_counts
