
import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def main():
    lengths = [8, 12, 16, 20]
    for length in lengths:
        print(f"Password (length {length}): {generate_password(length)}")


if __name__ == "__main__":
    main()
