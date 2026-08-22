
def sort_by_value(pairs):
    return sorted(pairs, key=lambda x: x[1])


def main():
    print(sort_by_value([('a', 3), ('b', 1), ('c', 2)]))

if __name__ == "__main__":
    main()
