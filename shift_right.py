
def shift_right(arr, k):
    k %= len(arr)
    return arr[-k:] + arr[:-k]


def main():
    print(shift_right([1, 2, 3, 4], 1))

if __name__ == "__main__":
    main()
