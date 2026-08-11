
def insertion_sort(arr):
    arr = arr.copy()
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def main():
    items = [12, 11, 13, 5, 6]
    print("Original:", items)
    print("Sorted:", insertion_sort(items))


if __name__ == "__main__":
    main()
