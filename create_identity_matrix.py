
def create_identity_matrix(size):
    return [[1 if i == j else 0 for j in range(size)] for i in range(size)]


def main():
    print(create_identity_matrix(4))

if __name__ == "__main__":
    main()
