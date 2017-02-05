import math

'''
By listing the first six prime numbers:
2, 3, 5, 7, 11, and 13, we can see that
the 6th prime is 13.

What is the 10001st prime number?
'''

def prime_10001():

    n =  int(2 * 10001 * math.log(10001))
    if n % 2 != 0: n += 1

    numbers = []
    numbers.extend([None, None])
    count = 0

    for i in range(2,n):
        numbers.append(True)

    for i, value in enumerate(numbers):
        if value == True:
            # sieve out non-primes by multiples of known primes
            for pos in range(2*i, n, i):
                numbers[pos] = False
            count += 1
        if count == 10001:
            print i
            return True
    return False


if __name__ == '__main__':
    prime_10001()
