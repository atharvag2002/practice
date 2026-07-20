
def transpose(matrix):
    return [list(row) for row in zip(*matrix)]


def main():
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print("Original:")
    for row in matrix:
        print(row)
    print("Transposed:")
    for row in transpose(matrix):
        print(row)


if __name__ == "__main__":
    main()
