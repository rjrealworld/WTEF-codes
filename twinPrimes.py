def is_prime(n):
    if n in {2,3,5,7}:
        return True
    if n%2==0 or n%3==0:
        return False
    else:
        r=5
        while r*r<=n:
            if n%r==0:
                return False
            r+=2
            if n%r==0:
                return False
            r+=4
    return True

def twin_prime(a,b):
    if a<=0 or b<=0:
        return -1
    elif a>=b:
        return -2
    a =  ((a+1) if (a%2==0) else a)
    prime=[]
    for i in range(a, b, 2):
        j=i+2
        if (is_prime(i) and is_prime(j)):
            twin=(i,j)
            prime.append(twin)
    if len(prime)==0:
        return -3
    return prime

print(twin_prime(1,20))
