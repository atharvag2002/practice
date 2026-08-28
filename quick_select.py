
def quick_select(arr, k):
    if len(arr) == 1:
        return arr[0]
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    if k < len(left):
        return quick_select(left, k)
    elif k < len(left) + len(middle):
        return middle[0]
    else:
        return quick_select(right, k - len(left) - len(middle))


def main():
    arrays = [
        ([3, 2, 1, 5, 6, 4], 2),
        ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4),
        ([1], 0)
    ]
    for arr, k in arrays:
        print(f"{arr}, k={k} -> {quick_select(arr, k)}")


if __name__ == "__main__":
    main()
