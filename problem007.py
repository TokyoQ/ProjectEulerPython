'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''
import math

MAX_NUM = 10001
primes = [2]
numPrimes = 1
i = 1

while numPrimes < MAX_NUM:
    i+=2
    divisible = ((i%j == 0) for j in range(2, int(math.ceil(math.sqrt(i))+1)))
    if not any(divisible):
        primes.append(i)
        numPrimes += 1
        #print i

print "The prime is: ", i