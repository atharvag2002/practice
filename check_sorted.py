
def is_sorted(arr, ascending=True):
    if ascending:
        return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))
    else:
        return all(arr[i] >= arr[i + 1] for i in range(len(arr) - 1))


def main():
    arrays = [
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [1, 3, 2, 4, 5]
    ]
    for arr in arrays:
        print(f"{arr} -> Ascending: {is_sorted(arr)}, Descending: {is_sorted(arr, False)}")


if __name__ == "__main__":
    main()
