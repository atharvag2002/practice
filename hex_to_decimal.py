
def hex_to_decimal(hex_str):
    hex_str = hex_str.upper().replace('0X', '')
    decimal = 0
    for i, char in enumerate(reversed(hex_str)):
        if char.isdigit():
            value = int(char)
        else:
            value = ord(char) - ord('A') + 10
        decimal += value * (16 ** i)
    return decimal


def main():
    hex_strings = ["1A", "FF", "100", "7F", "0"]
    for hex_str in hex_strings:
        print(f"0x{hex_str} -> {hex_to_decimal(hex_str)}")


if __name__ == "__main__":
    main()
