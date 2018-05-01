import random

def brutalPrime(n) :
    isPrime = True
    i = 2
    while (i < n/2) :   
        if n % i == 0 :
            isPrime = False
            return isPrime
        i = i + 1

    return isPrime

def pseudoPrimeMillerRabin(n) :
    k = 1000 
    i = 0
    isProbablyPrime = True
    while i<k :
        randomCheck = random.randint(2,(n-2))
        if (n % randomCheck) == 0 :
            isProbablyPrime = False
            return isProbablyPrime
        i = i + 1

    return isProbablyPrime

print("")
print("Enter the parameter tuple (p,q,g) : ")
print("Enter value for p : ")
p = long(raw_input())
print("Enter value for q : ")
q = long(raw_input())
print("Enter value for g : ")
g = long(raw_input())
print("")
print("Here's how good the DSA tuple is -> ")
print("According to brute-force primality testing is q prime ?")
print(brutalPrime(q))
print("")
print("According to Miller-Rabin primality testing, q is most probably prime ?")
print(pseudoPrimeMillerRabin(q))

print("")
print("Is g of the right form i.e. (h^((p-1)/q) mod p) where h = 2 ?")
h = 2
complexExponent = ((p-1) / q)
if (pow(h,complexExponent) % p) == g :
    print("True")
else :
    print("False")
print("")
