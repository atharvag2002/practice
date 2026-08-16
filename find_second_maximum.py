
def find_second_maximum(numbers):
    unique = sorted(set(numbers), reverse=True)
    return unique[1] if len(unique) > 1 else None


def main():
    print(find_second_maximum([1, 3, 4, 4, 2]))

if __name__ == "__main__":
    main()
