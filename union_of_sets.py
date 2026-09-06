
def union_of_sets(*sets):
    result = set()
    for s in sets:
        result.update(s)
    return result


def main():
    set_groups = [
        ({1, 2, 3}, {3, 4, 5}, {5, 6, 7}),
        ({'a', 'b'}, {'b', 'c'}, {'c', 'd'}),
        ({1, 2}, {3, 4})
    ]
    for group in set_groups:
        print(f"Union of {group} -> {union_of_sets(*group)}")


if __name__ == "__main__":
    main()
