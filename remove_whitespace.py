
def remove_whitespace(text):
    return ''.join(text.split())


def main():
    print(remove_whitespace(' hello world '))

if __name__ == "__main__":
    main()
