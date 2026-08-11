
def duplicate_values(items):
    seen = set()
    duplicates = set()
    for item in items:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    return list(duplicates)


def main():
    print(duplicate_values([1, 2, 2, 3, 3, 4]))

if __name__ == "__main__":
    main()
