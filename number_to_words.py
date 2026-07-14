
def number_to_words(n):
    words = {0:'zero',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten'}
    return words.get(n, str(n))


def main():
    print(number_to_words(7))
    print(number_to_words(12))

if __name__ == "__main__":
    main()
