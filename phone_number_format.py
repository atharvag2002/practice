
def phone_number_format(digits):
    digits = ''.join(filter(str.isdigit, digits))
    return f'({digits[:3]}) {digits[3:6]}-{digits[6:]}' if len(digits) == 10 else digits


def main():
    print(phone_number_format('1234567890'))

if __name__ == "__main__":
    main()
