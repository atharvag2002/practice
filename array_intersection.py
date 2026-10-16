
def array_intersection(a, b):
    return [x for x in a if x in b]


def main():
    print(array_intersection([1, 2, 3], [2, 3, 4]))

if __name__ == "__main__":
    main()
