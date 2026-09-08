
def shift_left(arr, k):
    k %= len(arr)
    return arr[k:] + arr[:k]


def main():
    print(shift_left([1, 2, 3, 4], 1))

if __name__ == "__main__":
    main()
