#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print("Last digit of", end=" ")
print(f"{number}", end=" ")
print("is", end=" ")
if number < 0:
    print("-", end="")
print(abs(number) % 10, end=" ")
if number > 5:
    print("and is greater than 5")
elif number == 0:
    print("and is zero")
else:
    print("and is less than 6 and not 0")
