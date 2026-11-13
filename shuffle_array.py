
import random

def shuffle_array(arr):
    n = len(arr)
    for i in range(n - 1, 0, -1):
        j = random.randint(0, i)
        arr[i], arr[j] = arr[j], arr[i]
    return arr


def main():
    arrays = [[1, 2, 3, 4, 5], [10, 20, 30, 40], ['a', 'b', 'c']]
    for arr in arrays:
        print(f"Original: {arr}")
        print(f"Shuffled: {shuffle_array(arr.copy())}")


if __name__ == "__main__":
    main()
