
def bubble_sort(arr):
    arr = arr.copy()
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


def main():
    items = [5, 2, 9, 1, 5, 6]
    print("Original:", items)
    print("Sorted:", bubble_sort(items))


if __name__ == "__main__":
    main()
