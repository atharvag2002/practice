
def generate_pascal_triangle(rows):
    triangle = []
    for i in range(rows):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        triangle.append(row)
    return triangle


def main():
    print(generate_pascal_triangle(5))

if __name__ == "__main__":
    main()
