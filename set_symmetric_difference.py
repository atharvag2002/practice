
def set_symmetric_difference(a, b):
    return [x for x in a + b if (x in a) ^ (x in b)]


def main():
    print(set_symmetric_difference([1, 2], [2, 3]))

if __name__ == "__main__":
    main()
