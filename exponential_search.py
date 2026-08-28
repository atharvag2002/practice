
def exponential_search(arr, target):
    if arr[0] == target:
        return 0
    
    bound = 1
    while bound < len(arr) and arr[bound] < target:
        bound *= 2
    
    left = bound // 2
    right = min(bound, len(arr) - 1)
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def main():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    targets = [1, 5, 10, 11]
    for target in targets:
        print(f"Search {target} -> {exponential_search(arr, target)}")


if __name__ == "__main__":
    main()
