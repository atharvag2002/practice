
def selection_sort_recursive(arr, index=0):
    n = len(arr)
    if index == n:
        return arr
    
    min_idx = index
    for i in range(index + 1, n):
        if arr[i] < arr[min_idx]:
            min_idx = i
    
    arr[index], arr[min_idx] = arr[min_idx], arr[index]
    return selection_sort_recursive(arr, index + 1)


def main():
    arrays = [[64, 34, 25, 12, 22, 11, 90], [5, 1, 4, 2, 8]]
    for arr in arrays:
        print(f"Original: {arr}")
        print(f"Sorted: {selection_sort_recursive(arr.copy())}")


if __name__ == "__main__":
    main()
