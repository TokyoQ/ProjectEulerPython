'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

import math
from utils import getPrimesLessThan

NUM = 600851475143
theSum = 0
primes = []
for num in range(int(math.ceil(math.sqrt(NUM))),1,-1):
    if(NUM % num == 0):
        primes = getPrimesLessThan(num+1)
        if primes.__contains__(num):
            print "The number is:", num
            break