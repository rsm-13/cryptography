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

def areCoprime(a,b):   #Check if two integers, a & b, are coprime
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

def phi(p,q):     #Euler's Totient Function (n in terms of p & q)
    return(p-1) * (q-1)

def main(): #Run RSA Encryption & Decryption
    e = 65537
    pt = str(input("input pt"))
    p = int(input('p goes here'))
    q = int(input('q goes here'))
    n = p * q

    if areCoprime(e, phi(p,q)) == True:
        d = 0
        while (e * d) % phi(p,q) != 1:
            d += 1

    encrypted = ''
    decrypted = ''
    for char in pt:
        m = ord(char)
        encrypted += str(m)
        c = (m ** e) % n
        decrypted += chr((c ** d) % n)
    
    print("Encrypted: " + str(encrypted))
    return "Decrypted: " + str(decrypted)

print(main())
