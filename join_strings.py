
def join_strings(strings, delimiter=','):
    return delimiter.join(strings)


def main():
    print(join_strings(['a', 'b', 'c'], '-'))

if __name__ == "__main__":
    main()
