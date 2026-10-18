
def reverse_list(items):
    reversed_items = []
    for item in items:
        reversed_items.insert(0, item)
    return reversed_items


def main():
    items = [1, 2, 3, 4, 5]
    print("Original:", items)
    print("Reversed:", reverse_list(items))


if __name__ == "__main__":
    main()
