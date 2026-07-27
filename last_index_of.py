
def last_index_of(items, value):
    for i in range(len(items)-1, -1, -1):
        if items[i] == value:
            return i
    return -1


def main():
    print(last_index_of([1, 2, 3, 2], 2))

if __name__ == "__main__":
    main()
