
def max_subarray_sum(numbers):
    max_ending = max_so_far = numbers[0]
    for n in numbers[1:]:
        max_ending = max(n, max_ending + n)
        max_so_far = max(max_so_far, max_ending)
    return max_so_far


def main():
    print(max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]))

if __name__ == "__main__":
    main()
