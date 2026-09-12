
def linear_search(arr, target):
    for i, element in enumerate(arr):
        if element == target:
            return i
    return -1


def main():
    arrays = [
        [10, 20, 30, 40, 50],
        [5, 3, 7, 1, 9],
        ['a', 'b', 'c', 'd']
    ]
    targets = [30, 7, 'c', 99]
    for arr, target in zip(arrays, targets):
        print(f"Search {target} in {arr} -> {linear_search(arr, target)}")


if __name__ == "__main__":
    main()
