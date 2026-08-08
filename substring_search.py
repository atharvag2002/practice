
def substring_search(text, pattern):
    for i in range(len(text) - len(pattern) + 1):
        if text[i:i+len(pattern)] == pattern:
            return i
    return -1


def main():
    print(substring_search('hello world', 'world'))

if __name__ == "__main__":
    main()
