'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''
import math
from utils import getPrimesLessThan
MAGIC_NUM = 2000000

primes = getPrimesLessThan(MAGIC_NUM)
print "The sum is: ", sum(primes)