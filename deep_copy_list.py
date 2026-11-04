
def deep_copy_list(lst):
    if not isinstance(lst, list):
        return lst
    return [deep_copy_list(item) for item in lst]


def main():
    original = [1, [2, 3], [4, [5, 6]]]
    copy = deep_copy_list(original)
    copy[1][0] = 99
    print(f"Original: {original}")
    print(f"Copy: {copy}")


if __name__ == "__main__":
    main()
