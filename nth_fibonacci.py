
def nth_fibonacci(n):
    if n <= 1:
        return n
    
    def matrix_multiply(a, b):
        return [
            [a[0][0] * b[0][0] + a[0][1] * b[1][0],
             a[0][0] * b[0][1] + a[0][1] * b[1][1]],
            [a[1][0] * b[0][0] + a[1][1] * b[1][0],
             a[1][0] * b[0][1] + a[1][1] * b[1][1]]
        ]
    
    def matrix_pow(mat, power):
        result = [[1, 0], [0, 1]]
        while power > 0:
            if power % 2 == 1:
                result = matrix_multiply(result, mat)
            mat = matrix_multiply(mat, mat)
            power //= 2
        return result
    
    base = [[1, 1], [1, 0]]
    result = matrix_pow(base, n - 1)
    return result[0][0]


def main():
    numbers = [0, 1, 5, 10, 20, 50, 100]
    for n in numbers:
        print(f"fib({n}) = {nth_fibonacci(n)}")


if __name__ == "__main__":
    main()
