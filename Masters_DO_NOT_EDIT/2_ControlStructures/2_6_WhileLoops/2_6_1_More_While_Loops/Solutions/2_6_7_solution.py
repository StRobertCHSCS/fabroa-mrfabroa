
max = 0
number = int(input("Enter a number: "))

while number != 0:
    if number > max:
        max = number
    number = int(input("Enter a number: "))

print(max)