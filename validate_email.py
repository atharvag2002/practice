
def validate_email(email):
    return '@' in email and '.' in email.split('@')[-1]


def main():
    print(validate_email('test@example.com'))
    print(validate_email('invalid-email'))

if __name__ == "__main__":
    main()
