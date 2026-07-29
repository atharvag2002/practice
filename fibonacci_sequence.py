
def fibonacci(n):
    if n <= 0:
        return []
    if n == 1:
        return [0]

    seq = [0, 1]
    while len(seq) < n:
        seq.append(seq[-1] + seq[-2])
    return seq


def main():
    n = 10
    print(f"First {n} Fibonacci numbers:")
    print(fibonacci(n))


if __name__ == "__main__":
    main()
