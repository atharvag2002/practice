
def ascii_values(text):
    return {char: ord(char) for char in text}


def main():
    print(ascii_values('abc'))

if __name__ == "__main__":
    main()
