
def permutations_of_list(items):
    if len(items) <= 1:
        return [items]
    result = []
    for i, item in enumerate(items):
        for perm in permutations_of_list(items[:i] + items[i+1:]):
            result.append([item] + perm)
    return result


def main():
    print(permutations_of_list([1, 2, 3]))

if __name__ == "__main__":
    main()
