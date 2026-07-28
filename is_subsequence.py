
def is_subsequence(s, t):
    it = iter(t)
    return all(ch in it for ch in s)


def main():
    print(is_subsequence('abc', 'ahbgdc'))
    print(is_subsequence('axc', 'ahbgdc'))

if __name__ == "__main__":
    main()
