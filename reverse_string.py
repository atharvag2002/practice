
def reverse_string(s):
    return s[::-1]


def reverse_iterative(s):
    result = []
    for ch in s:
        result.insert(0, ch)
    return ''.join(result)


def main():
    sample = "hello world"
    print(f"Original: {sample}")
    print(f"Reversed: {reverse_string(sample)}")
    print(f"Reversed iterative: {reverse_iterative(sample)}")


if __name__ == "__main__":
    main()
