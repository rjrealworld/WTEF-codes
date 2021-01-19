#Euler’s Totient function for an input n is the count of numburs in
#[1, 2, 3, ...n] that are relatively prime to n

def gcd(a, b): 
    if (a == 0): 
        return b 
    return gcd(b % a, a) 
                  
def phi(n): 
    result = 1
    for i in range(2, n): 
        if (gcd(i, n) == 1):
            result += 1
    return result 

n = int(input())
print("phi(", n, ") = ", phi(n), sep = "") 
