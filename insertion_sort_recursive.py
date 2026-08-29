
def insertion_sort_recursive(arr, n=None):
    if n is None:
        n = len(arr)
    if n <= 1:
        return arr
    
    insertion_sort_recursive(arr, n - 1)
    
    key = arr[n - 1]
    j = n - 2
    
    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j -= 1
    
    arr[j + 1] = key
    return arr


def main():
    arrays = [[12, 11, 13, 5, 6], [64, 34, 25, 12, 22, 11, 90]]
    for arr in arrays:
        print(f"Original: {arr}")
        print(f"Sorted: {insertion_sort_recursive(arr.copy())}")


if __name__ == "__main__":
    main()
