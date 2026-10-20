
def list_chunking(items, k):
    return [items[i:i+k] for i in range(0, len(items), k)]


def main():
    print(list_chunking([1, 2, 3, 4, 5], 2))

if __name__ == "__main__":
    main()
