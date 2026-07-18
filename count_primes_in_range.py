
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


def count_primes_in_range(start, end):
    return sum(1 for n in range(start, end + 1) if is_prime(n))


def main():
    print(count_primes_in_range(1, 20))

if __name__ == "__main__":
    main()
