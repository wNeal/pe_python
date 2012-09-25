#! /usr/bin/env python
"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?

I chose to solve this using a sieve of Eratosthenes
I also use the bitarray module to create a more efficient sieve
"""
from bitarray import bitarray

TARGET = 600851475143
#MAX_BOUND = TARGET / 2
MAX_BOUND = 50000

# Create and initialize the sieve
sieve = bitarray(MAX_BOUND)
sieve.setall(False)

def process_sieve():
    # Loop over the sieve and find
    for x in range(2, MAX_BOUND):
        current_index = x - 2
        if sieve[current_index]:
            continue    # Get the next prime
        else:
            for num in range(x + 1, len(sieve)):
                if not sieve[num - 2] and (num % x) == 0:
                    sieve[num - 2] ^= 1   # This number isn't prime so flip its bit

def isMultiple(num):
    if (TARGET % num) == 0:
        return True
    return False

def main():
    largest_multiple = 1
    process_sieve()

    for i in range(2, len(sieve) ):
        if not sieve[i - 2] and isMultiple(i):
            print( i )
            largest_multiple = i

    return largest_multiple

if __name__ == "__main__":
    print( main() )
