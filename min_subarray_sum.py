
def min_subarray_sum(numbers):
    min_ending = min_so_far = numbers[0]
    for n in numbers[1:]:
        min_ending = min(n, min_ending + n)
        min_so_far = min(min_so_far, min_ending)
    return min_so_far


def main():
    print(min_subarray_sum([2, -1, 3, -4, 5]))

if __name__ == "__main__":
    main()
