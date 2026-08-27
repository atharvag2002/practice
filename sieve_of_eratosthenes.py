
def sieve_of_eratosthenes(n):
    if n < 2:
        return []
    
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    
    return [i for i, is_prime in enumerate(sieve) if is_prime]


def main():
    numbers = [10, 30, 50, 100]
    for n in numbers:
        print(f"Primes up to {n}: {sieve_of_eratosthenes(n)}")


if __name__ == "__main__":
    main()
