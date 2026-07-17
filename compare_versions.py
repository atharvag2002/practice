
def compare_versions(a, b):
    parts_a = [int(x) for x in a.split('.')]
    parts_b = [int(x) for x in b.split('.')]
    for x, y in zip(parts_a, parts_b):
        if x != y:
            return x - y
    return len(parts_a) - len(parts_b)


def main():
    print(compare_versions('1.2.0', '1.2'))
    print(compare_versions('1.2.1', '1.2.0'))

if __name__ == "__main__":
    main()
