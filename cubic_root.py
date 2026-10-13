
def cubic_root(n):
    if n >= 0:
        return n ** (1/3)
    else:
        return -((-n) ** (1/3))


def main():
    numbers = [-27, -8, -1, 0, 1, 8, 27, 64]
    for num in numbers:
        print(f"cubic_root({num}) = {cubic_root(num):.4f}")


if __name__ == "__main__":
    main()
