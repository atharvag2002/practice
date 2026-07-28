
from itertools import permutations

def string_permutations(s):
    return [''.join(p) for p in permutations(s)]


def main():
    print(string_permutations("abc"))


if __name__ == "__main__":
    main()
