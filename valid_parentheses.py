
def is_valid_parentheses(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping:
            if not stack or stack.pop() != mapping[char]:
                return False
        else:
            continue
    
    return len(stack) == 0


def main():
    strings = ["()", "()[]{}", "(]", "([{}])", "", "((("]
    for s in strings:
        print(f"'{s}' -> {is_valid_parentheses(s)}")


if __name__ == "__main__":
    main()
