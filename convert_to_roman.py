
def to_roman(num):
    val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    syms = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    result = []
    for i, v in enumerate(val):
        while num >= v:
            result.append(syms[i])
            num -= v
    return ''.join(result)


def main():
    numbers = [1, 4, 9, 58, 1994, 3999]
    for num in numbers:
        print(f"{num} -> {to_roman(num)}")


if __name__ == "__main__":
    main()
