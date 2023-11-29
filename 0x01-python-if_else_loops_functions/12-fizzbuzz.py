#!/usr/bin/python3

"""
prints the numbers from 1 to 100 separated by a space
For multiples of three print Fizz
For multiples of five print Buzz
For numbers which are multiples of both three and five
print FizzBuzz
"""


def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end=" ")
        elif i % 3 == 0:
	        print("Fizz", end=" ")
        elif i % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(i, end=" ")
