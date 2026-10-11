
import base64

def base64_encode(text):
    return base64.b64encode(text.encode()).decode()


def main():
    strings = ["Hello", "World", "Test123", "Python"]
    for s in strings:
        print(f"{s} -> {base64_encode(s)}")


if __name__ == "__main__":
    main()
