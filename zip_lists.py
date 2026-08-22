
def zip_lists(a, b):
    return [(a[i], b[i]) for i in range(min(len(a), len(b)))]


def main():
    print(zip_lists([1, 2], ['a', 'b']))

if __name__ == "__main__":
    main()
