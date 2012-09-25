import unittest

import sieve_of_atkin


class SieveOfAtkinTest(unittest.TestCase):
    """the sieve of atkin should return a valid list of prime numbers up until
    the number provided
    """
    primes_sieve = sieve_of_atkin.SieveOfAtkin(1000000)

    def test_prime_output(self):
        """verify that the output of primes matches known values
        """
        with open('primes.txt', encoding='utf-8') as primes:
            for line in primes:
                result = self.primes_sieve.is_prime(int(line))
                self.assertEqual(True, result)

    def test_nth_prime(self):
        """verify that the nth prime matches known nth prime
        """
        with open('primes.txt', encoding='utf-8') as  primes:
            prime_count = 1
            for line in primes:
                result = self.primes_sieve.get_nth_prime(prime_count)
                self.assertEqual(int(line), result)
                prime_count += 1


if __name__ == '__main__':
    unittest.main()

