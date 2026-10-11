
def xor_operation(n, start):
    nums = [start + 2 * i for i in range(n)]
    result = 0
    for num in nums:
        result ^= num
    return result


def main():
    test_cases = [
        (5, 0),
        (4, 3),
        (1, 7),
        (10, 5)
    ]
    for n, start in test_cases:
        print(f"XOR of array from {start} with {n} elements: {xor_operation(n, start)}")


if __name__ == "__main__":
    main()
