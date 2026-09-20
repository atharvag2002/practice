
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def list_primes(limit):
    return [x for x in range(2, limit + 1) if is_prime(x)]


def main():
    print("Primes up to 50:", list_primes(50))
    for num in [1, 2, 17, 18, 19, 20, 23, 24]:
        print(f"{num} is prime? {is_prime(num)}")


if __name__ == "__main__":
    main()
