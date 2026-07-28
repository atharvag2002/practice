
def longest_common_prefix(strings):
    if not strings:
        return ''
    prefix = strings[0]
    for s in strings[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ''
    return prefix


def main():
    print(longest_common_prefix(['flower', 'flow', 'flight']))

if __name__ == "__main__":
    main()
