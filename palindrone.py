# Add palindrome checker

text = input("Enter a string: ")

clean = text.lower().replace(" ", "")

if clean == clean[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")