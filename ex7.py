#! /usr/bin/env python
"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?
"""
from sieve_of_atkin import SieveOfAtkin

def main():
    primes_sieve = SieveOfAtkin(100000)

    return primes_sieve.get_nth_prime(10001)

if __name__ == '__main__':
    print(main())
