
def remove_all_occurrences(lst, value):
    return [item for item in lst if item != value]


def main():
    test_cases = [
        ([1, 2, 3, 2, 4, 2, 5], 2),
        (['a', 'b', 'a', 'c'], 'a'),
        ([1, 1, 1, 1], 1)
    ]
    for lst, value in test_cases:
        print(f"{lst}, remove {value} -> {remove_all_occurrences(lst, value)}")


if __name__ == "__main__":
    main()
