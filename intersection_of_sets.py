
def intersection_of_sets(*sets):
    if not sets:
        return set()
    result = set(sets[0])
    for s in sets[1:]:
        result.intersection_update(s)
    return result


def main():
    set_groups = [
        ({1, 2, 3}, {2, 3, 4}, {3, 4, 5}),
        ({'a', 'b'}, {'b', 'c'}, {'b', 'd'}),
        ({1, 2}, {3, 4})
    ]
    for group in set_groups:
        print(f"Intersection of {group} -> {intersection_of_sets(*group)}")


if __name__ == "__main__":
    main()
