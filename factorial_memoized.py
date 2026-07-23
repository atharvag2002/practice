
cache = {}

def factorial_memoized(n):
    if n in cache:
        return cache[n]
    if n <= 1:
        return 1
    cache[n] = n * factorial_memoized(n - 1)
    return cache[n]


def main():
    print(factorial_memoized(10))

if __name__ == "__main__":
    main()
