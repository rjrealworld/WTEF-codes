import math

def reverse (n: int) -> str :
    return str(n)[::-1]

def is palindrome (n: str) -> bool:
    return n == reverse(n)

def is_prfct_sq(n) -> bool :
    sqr_rt = math.sqrt(n)
    return int(sqr_rt) == sqr_rt

def all_digits_even(n) -> bool :
    while n>0:
        if n % 2 != 0:
            return False
        n = n//10
    return True

for i in range(1000,10000):
    if (is_prfct_sq(i) and all_digits_even(i)):
        print(i)
