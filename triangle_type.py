
def triangle_type(a, b, c):
    if a == b == c:
        return 'equilateral'
    if a == b or b == c or a == c:
        return 'isosceles'
    return 'scalene'


def main():
    print(triangle_type(3, 3, 3))
    print(triangle_type(3, 4, 5))

if __name__ == "__main__":
    main()
