#! /usr/bin/env python
"""
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""
from tkinter import *

MAX = 100

def sum_of_squares(max_num):
    sum = 0
    for num in range(1,max_num + 1):
        sum += num**2
    return sum

def square_of_sums(max_num):
    sum = 0
    for num in range(1,max_num + 1):
        sum += num
    return sum**2

def main():
    return square_of_sums(MAX) - sum_of_squares(MAX)


if __name__ == "__main__":
    result = main()

    # Copy the result to the clipboard
    r = Tk()
    r.withdraw()
    r.clipboard_clear()
    r.clipboard_append(result)

    print(result)
    r.mainloop()
