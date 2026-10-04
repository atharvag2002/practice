
def element_frequency(lst):
    freq = {}
    for item in lst:
        freq[item] = freq.get(item, 0) + 1
    return freq


def main():
    lists = [
        [1, 2, 2, 3, 3, 3, 4],
        ['a', 'b', 'a', 'c', 'b', 'a'],
        [1, 1, 1, 1]
    ]
    for lst in lists:
        print(f"{lst} -> {element_frequency(lst)}")


if __name__ == "__main__":
    main()
