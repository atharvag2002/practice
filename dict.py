
count = {}

for number in numbers:
    if number in count:
        count[number] += 1
    else:
        count[number] = 1

print(count)