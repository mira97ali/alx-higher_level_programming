#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print("Last digit of", end=" ")
print(f"{number}", end=" ")
print("is", end=" ")
print(str(number)[-1], end=" ")
if number > 5:
    print("is greater than 5")
elif number == 0:
    print("is zero")
else:
    print("is less than 6 and not 0")
