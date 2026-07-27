
def has_duplicates(items):
    return len(items) != len(set(items))


def main():
    print(has_duplicates([1, 2, 3, 2]))
    print(has_duplicates([1, 2, 3]))

if __name__ == "__main__":
    main()
