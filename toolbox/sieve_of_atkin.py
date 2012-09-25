from bitarray import bitarray
from math import sqrt

class OutOfRangeError(ValueError): pass

class SieveOfAtkin:
    """the sieve of Atkin is a fast, modern algorithm for finding all prime numbers up to a specified integer
    0 values in the sieve represent prime numbers
    """

    def __init__(self, limit):
        # Set the arbitrary search limit
        self.limit = limit

        # Initialize the sieve
        self.sieve = bitarray(self.limit)
        self.sieve.setall(False)

        # Put in canidate primes:
        # integers which have an odd number of
        # representations by certain quadratic forms
        sqrt_limit = int(sqrt(limit))
        for x in range(1, sqrt_limit):
            x_square = x * x
            for y in range(1, sqrt_limit):
                y_square = y * y
                n = 4 * x_square + y_square
                if n <= limit and (n % 12 == 1 or n % 12 == 5):
                    self.sieve[n] ^= True      # Not prime, set flag

                x_square_times_3 = 3 * x_square
                n = x_square_times_3 + y_square
                if (n <= limit) and (n % 12 == 7):
                    self.sieve[n] ^= True      # Not prime, set flag

                n = x_square_times_3 - y_square
                if (x > y) and (n <= limit) and (n % 12 == 11):
                    self.sieve[n] ^= True      # Not prime, set flag

        # Enable composites by sieving
        self.sieve[2] = True        # 2
        self.sieve[3] = True        # 3
        for n in range(5, sqrt_limit + 1):
            if self.sieve[n]:
                # n is prime, omit multiples of its square; this is
                # sufficient because composites which managed to get
                # on the list cannot be square-free
                n_square = n * n
                for k in range(n_square, sqrt_limit + 1, n_square):
                    self.sieve[k] = False

    def is_prime(self, index):
        """checks primality of the index provided
        """
        return self.sieve[index]

    def get_nth_prime(self, n):
        """get the nth prime number
        """
        prime_count = 0
        for i in range(len(self.sieve) - 1):
            if self.sieve[i]:
                prime_count += 1

            if prime_count == n:
                return i

        raise OutOfRangeError
