
def swap_elements(arr, i, j):
    arr = arr.copy()
    arr[i], arr[j] = arr[j], arr[i]
    return arr


def main():
    print(swap_elements([1, 2, 3], 0, 2))

if __name__ == "__main__":
    main()
