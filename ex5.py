#! /usr/bin/env python
"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""


def main():
    curr = 2520     # our current number. let's start at 2520
    (test_numbers, largest_num) = simplify_divisors(list(range(1,21)))
    test_numbers_length = len(test_numbers)

    while True:
        divisors = set()
        for num in test_numbers:
            if curr % num != 0:
                break
            else:
                divisors.add(num)
        if divisors and len(divisors) == test_numbers_length:
            break
        curr += largest_num       # it must be even
    return curr

def simplify_divisors(d_list):
    d_list.sort()
    largest = d_list[-1]
    d_set = set(d_list)

    # Remove any factors
    for d in d_list:
        for f in d_list:
            if d != f and d % f == 0:
                d_set.discard(f)
    return (d_set, largest)


if __name__ == "__main__":
    print(main())
