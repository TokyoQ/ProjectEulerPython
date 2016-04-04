import math

# Return factorial of n
def fact(n):
    if n==1 or n==0:
        return 1
    else:
        return n * fact(n-1)
    
# Return list of all proper divisors of n
def getDivisors(n):
    divisors = []
    for i in range(1,int(math.ceil(n/2))+1):
        if n%i==0:
            divisors.append(i)
    return divisors

# Return the sum of all proper divisors of n
def sumProperDivisors(n):
    return sum(getDivisors(n))

# Return a list of all primes less than n using the Sieve of Eratosthenes
def getPrimesLessThan(n):
    primes = []
    marked = [False]*n
    
    for i in range(2,n):
        if not marked[i]:
            
            #Add to list of primes and mark all multiples
            primes.append(i)
            for j in range(i,n,i):
                marked[j] = True
                
    return primes

def isAbundant(n):
    return sumProperDivisors(n) > n

def isPalindrome(inp):
    return str(inp) == str(inp)[::-1]

def arrProd(inp):
    return reduce( (lambda x, y: x * y), inp )

