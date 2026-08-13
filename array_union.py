
def array_union(a, b):
    result = list(a)
    for item in b:
        if item not in result:
            result.append(item)
    return result


def main():
    print(array_union([1, 2], [2, 3, 4]))

if __name__ == "__main__":
    main()
