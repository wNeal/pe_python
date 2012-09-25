#! /usr/bin/env python
"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91  99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""

def get_rev(num):
    """ reverse an integer """
    rev = 0
    while num > 0:
        dig = num % 10          # get the last digit
        rev = rev * 10 + dig    # append the new digit
        num = int(num / 10)     # remove the last digit from the tmp

    return rev

def product_gen():
    """ generate the product of 2 three digit numbers """
    a = b = 999         # init a, b
    while a > 99:
        yield a,  b
        if b == 100:
            b = a = a - 1
        else:
            b -= 1

def main():
    curr = 0
    best = (0, 0, 0)
    g = product_gen()
    for x, y in g:
       curr = x * y
       rev = get_rev(curr)
       if curr == rev and curr > best[0]:
           best = (curr, x, y)

    print( "curr: {}, x: {}, y:{}".format(*best) )

if __name__ == "__main__":
    main()
