
def accumulate_sum(numbers):
    totals = []
    current = 0
    for value in numbers:
        current += value
        totals.append(current)
    return totals


def main():
    print(accumulate_sum([1, 2, 3, 4, 5]))

if __name__ == "__main__":
    main()
