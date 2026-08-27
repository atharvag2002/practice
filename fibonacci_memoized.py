
cache = {0: 0, 1: 1}

def fibonacci_memoized(n):
    if n in cache:
        return cache[n]
    cache[n] = fibonacci_memoized(n-1) + fibonacci_memoized(n-2)
    return cache[n]


def main():
    print([fibonacci_memoized(i) for i in range(10)])

if __name__ == "__main__":
    main()
