
from itertools import combinations

def string_combinations(s, length):
    return [''.join(c) for c in combinations(s, length)]


def main():
    print(string_combinations("abcd", 2))


if __name__ == "__main__":
    main()
