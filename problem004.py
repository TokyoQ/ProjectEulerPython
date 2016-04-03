'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''
from utils import isPalindrome

maxNum = 0
for i in range(999,100,-1):
    for j in range(999,100,-1):
        prod = i*j
        if isPalindrome(prod):
            maxNum = max(prod, maxNum)
        
print "Max is:", maxNum