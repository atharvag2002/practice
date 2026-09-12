
def sort_by_length(strings):
    return sorted(strings, key=len)


def main():
    print(sort_by_length(['apple', 'pear', 'banana', 'kiwi']))

if __name__ == "__main__":
    main()
