
def cyclic_rotation(arr, k):
    k %= len(arr)
    return arr[-k:] + arr[:-k]


def main():
    print(cyclic_rotation([1, 2, 3, 4, 5], 2))

if __name__ == "__main__":
    main()
