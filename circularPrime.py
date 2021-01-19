def is_even(n: int) -> bool:
    if n%2==0:
        return True
    return False

def is_prime(n: int) -> bool:
    if n == 2:
        return True
    if is_even(n):
        return False
    else:
        r=3
        while r*r<=n:
            if n%r==0:
                return False
            r+=2
    return True

def rotation(string_number: str) -> [str]:
    return ([string_number[i:]+string_number[:i] for i in range(len(string_number))])

def isCircularPrime(num):
    if num in {2,3,5,7}:
        return True
    elif is_even(num):
        return False
    else:
        for number in rotation(str(num)):
            if not is_prime(int(number)):
                return False
    return True
print(isCircularPrime(1))