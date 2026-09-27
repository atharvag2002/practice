
def octal_to_decimal(octal_str):
    decimal = 0
    for i, char in enumerate(reversed(octal_str)):
        decimal += int(char) * (8 ** i)
    return decimal


def main():
    octal_strings = ["0", "7", "10", "17", "100", "777"]
    for oct_str in octal_strings:
        print(f"Octal {oct_str} -> Decimal {octal_to_decimal(oct_str)}")


if __name__ == "__main__":
    main()
