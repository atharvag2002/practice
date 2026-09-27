
def validate_ip(address):
    parts = address.split('.')
    if len(parts) != 4:
        return False
    for part in parts:
        if not part.isdigit() or not 0 <= int(part) <= 255:
            return False
    return True


def main():
    print(validate_ip('192.168.0.1'))
    print(validate_ip('999.999.999.999'))

if __name__ == "__main__":
    main()
