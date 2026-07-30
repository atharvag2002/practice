
def set_difference(a, b):
    return [x for x in a if x not in b]


def main():
    print(set_difference([1, 2, 3], [2, 4]))

if __name__ == "__main__":
    main()
