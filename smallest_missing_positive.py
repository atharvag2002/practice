
def smallest_missing_positive(numbers):
    s = set(numbers)
    i = 1
    while i in s:
        i += 1
    return i


def main():
    print(smallest_missing_positive([3, 4, -1, 1]))

if __name__ == "__main__":
    main()
