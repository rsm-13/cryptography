def isPrime(n): #Check if the number is prime
    for i in range(2,int(n**0.5)+1):
        #If a remainder, not prime
        if (n % i) == 0:
            return str(False) + " (not prime)"
    #If negative, not prime
    if n <= 1:
        return str(False) + " (not prime)"
    #If no remainder, prime
    else:
        return str(True) + " (is prime)"

def primeFactors(n):    #Find the prime factors of n
    factors = [i for i in range(1,n) if (n % i) == 0]
    
    primes = []
    for i in range(len(factors)):
        test = isPrime(factors[i])
        if test == True:
            primes.append(factors[i])
    return primes

def primeFactorization(n):  #Find the prime factorization of an int, n
    factors = []
   
    #check if it is an even number
    while n % 2 == 0:
        factors.append(2)
        n = n / 2
    
    #if the new n is odd
    for i in range(3, int(n**0.5)+1, 2):
        while (n % i) == 0:
            factors.append(i)
            n = n / i
    
    if n > 2:
        factors.append(n)
    
    return factors

def areCoprime(a, b):   #Check if two integers, a & b, are coprime
    #Get factors of a and b using prime factorization
    a_factors = primeFactorization(a)
    b_factors = primeFactorization(b)

    result = True
    for x in a_factors:
        for y in b_factors:
            #If two elements are the same, then they are not coprime
            if x == y:
                result = False

    return result

def phi(n):     #Euler's Totient Function
    #Find all ints < n which are coprime with n

    i = 1
    coprimes = []
    #Repeat for all ints less than n
    while i < n:
        #Check if i & n are coprime
        result = areCoprime(i,n)
        #If the two are coprime, add it to the list
        if result == True:
            coprimes.append(i)
        i += 1
    
    return len(coprimes) #Return the number of coprime numbers

n = int(input("input n "))
#print(isPrime(n))
#print(primeFactorization(n))
#print(areCoprime(a,b))
print(phi(n))