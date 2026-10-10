
def perimeter_of_rectangle(length, width):
    return 2 * (length + width)


def main():
    rectangles = [(5, 3), (10, 4), (7, 7), (2, 8)]
    for length, width in rectangles:
        print(f"Rectangle {length}x{width} -> Perimeter: {perimeter_of_rectangle(length, width)}")


if __name__ == "__main__":
    main()
