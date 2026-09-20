
def fizzbuzz_extended(n, rules):
    result = []
    for i in range(1, n + 1):
        output = ""
        for divisor, word in rules:
            if i % divisor == 0:
                output += word
        result.append(output if output else str(i))
    return result


def main():
    rules = [(3, "Fizz"), (5, "Buzz"), (7, "Bazz")]
    n = 20
    print(f"FizzBuzzExtended (n={n}):")
    for i, val in enumerate(fizzbuzz_extended(n, rules), 1):
        print(f"{i}: {val}")


if __name__ == "__main__":
    main()
