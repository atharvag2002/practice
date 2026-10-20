
def reverse_dictionary(d):
    return {value: key for key, value in d.items()}


def main():
    print(reverse_dictionary({'a': 1, 'b': 2}))

if __name__ == "__main__":
    main()
