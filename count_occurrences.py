
def count_occurrences(items, value):
    count = 0
    for item in items:
        if item == value:
            count += 1
    return count


def main():
    print(count_occurrences([1, 2, 2, 3, 2], 2))

if __name__ == "__main__":
    main()
