
def remove_duplicates(items):
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


def main():
    items = [1, 2, 2, 3, 4, 1, 5]
    print("Original:", items)
    print("Without duplicates:", remove_duplicates(items))


if __name__ == "__main__":
    main()
