
def string_to_integer(s):
    s = s.strip()
    if not s:
        return 0
    
    sign = 1
    index = 0
    
    if s[0] == '-':
        sign = -1
        index = 1
    elif s[0] == '+':
        index = 1
    
    result = 0
    while index < len(s) and s[index].isdigit():
        digit = int(s[index])
        result = result * 10 + digit
        index += 1
    
    result *= sign
    
    if result < -2**31:
        return -2**31
    if result > 2**31 - 1:
        return 2**31 - 1
    
    return result


def main():
    strings = ["42", "   -42", "4193 with words", "words and 987", ""]
    for s in strings:
        print(f"'{s}' -> {string_to_integer(s)}")


if __name__ == "__main__":
    main()
