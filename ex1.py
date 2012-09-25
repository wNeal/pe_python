#! /usr/bin/env python

""" Problem 1
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""

ints = [3,5]

def main():
    sum = 0
    for x in range(1, 1000):
        if isMultiple(x):
            sum += x
    return sum

def isMultiple(num):
    for int in ints:
        if (num % int) == 0:
            return True
    return False


if __name__ == "__main__":
    print( main() )
