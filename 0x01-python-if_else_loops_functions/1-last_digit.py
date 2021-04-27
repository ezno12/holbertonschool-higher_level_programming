#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
x = number % 10
if number < 0:
    x = abs(number) % 10
    x *= -1
print("Last x of", end=' ')
if x > 5:
    print("{:d} is {:d} and is greater than 5".format(number, x))
elif x == 0:
    print("{:d} is {:d} and is 0".format(number, x))
else:
    print("{:d} is {:d} and is less than 6 and not 0".format(number, x))
