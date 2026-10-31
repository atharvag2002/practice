
def missing_number(numbers):
    n = len(numbers) + 1
    total = n * (n + 1) // 2
    return total - sum(numbers)


def main():
    print(missing_number([1, 2, 4, 5]))

if __name__ == "__main__":
    main()
