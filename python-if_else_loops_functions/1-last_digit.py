#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)

num_str = str(number)
if number < 0:
    last_digit = -int(num_str[-1])
else:
    last_digit = int(num_str[-1])

print("Last digit of", number, "is", last_digit, end='')

if last_digit > 5:
    print(" and is greater than 5")
elif last_digit == 0:
    print(" and is 0")
else:
    print(" and is less than 6 and not 0")
