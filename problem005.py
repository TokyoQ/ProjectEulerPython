'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

MAX_NUM = 20

i = 20
while(i<300000000):
    remainders = ((i%j==0) for j in range(1,MAX_NUM))
    #print "i:", i, " remainders:", remainders
    if all(remainders):
        print "The number is:", i
        break
    i+=MAX_NUM