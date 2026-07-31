
def rotate_matrix(matrix):
    return [list(reversed(col)) for col in zip(*matrix)]


def main():
    print(rotate_matrix([[1, 2], [3, 4]]))

if __name__ == "__main__":
    main()
