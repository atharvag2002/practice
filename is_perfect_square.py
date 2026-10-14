
def is_perfect_square(n):
    if n < 0:
        return False
    if n == 0:
        return True
    left, right = 1, n
    while left <= right:
        mid = (left + right) // 2
        square = mid * mid
        if square == n:
            return True
        elif square < n:
            left = mid + 1
        else:
            right = mid - 1
    return False


def main():
    numbers = [0, 1, 4, 9, 16, 25, 26, 100, 101]
    for num in numbers:
        print(f"{num} -> {is_perfect_square(num)}")


if __name__ == "__main__":
    main()
