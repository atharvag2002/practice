
def even_odd_partition(numbers):
    even = [n for n in numbers if n % 2 == 0]
    odd = [n for n in numbers if n % 2 != 0]
    return even, odd


def main():
    print(even_odd_partition([1, 2, 3, 4, 5, 6]))

if __name__ == "__main__":
    main()
