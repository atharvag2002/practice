
def power_set(items):
    result = [[]]
    for item in items:
        result += [curr + [item] for curr in result]
    return result


def main():
    print(power_set([1, 2, 3]))

if __name__ == "__main__":
    main()
