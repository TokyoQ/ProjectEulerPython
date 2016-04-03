# Return factorial of n
def fact(n):
    if n==1 or n==0:
        return 1
    else:
        return n * fact(n-1)
    
# Return the sum of all proper dividors of n
def sumProperDivisors(n):
    theSum = 0
    return theSum

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
