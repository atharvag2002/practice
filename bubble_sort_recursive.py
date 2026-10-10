
def bubble_sort_recursive(arr, n=None):
    if n is None:
        n = len(arr)
    if n == 1:
        return arr
    
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    
    return bubble_sort_recursive(arr, n - 1)


def main():
    arrays = [[64, 34, 25, 12, 22, 11, 90], [5, 1, 4, 2, 8]]
    for arr in arrays:
        print(f"Original: {arr}")
        print(f"Sorted: {bubble_sort_recursive(arr.copy())}")


if __name__ == "__main__":
    main()
