def count_fruits(fruits: list[str]) -> dict[str, int]:
    dict_counts = {}
    
    if len(fruits) == 0:
        return {}

    for fruit in fruits:
        
        #print(dict_counts.keys())
        if not fruit in dict_counts.keys():
            dict_counts[fruit] = 1
        else:
            dict_counts[fruit] += 1
    #print(dict_counts)
    return dict_counts


def main() -> None:
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
    assert count_fruits([]) == {}
    # add more tests


if __name__ == "__main__":
    main()
