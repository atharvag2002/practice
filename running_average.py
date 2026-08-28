
def running_average(numbers):
    totals = 0
    averages = []
    for i, num in enumerate(numbers, 1):
        totals += num
        averages.append(totals / i)
    return averages


def main():
    print(running_average([1, 2, 3, 4]))

if __name__ == "__main__":
    main()
