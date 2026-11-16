
def product_of_list(numbers):
    product = 1
    for number in numbers:
        product *= number
    return product


def main():
    print(product_of_list([1, 2, 3, 4]))

if __name__ == "__main__":
    main()
