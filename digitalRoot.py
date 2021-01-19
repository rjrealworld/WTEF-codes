def IsSpecialNumber(n):
    # YOUR CODE HERE
    i=0
    fact=1
    fact_list=[]
    diff_no=[]
    while n!=0:
        i=n%10
        n=n//10
        diff_no.append(i)
    for u in diff_no:
        x=u
        fact=1
        while x!=0:
            fact *=x
            x-=1
            fact_list.append(fact)
    sum=0
    for x in fact_list:
        sum+=x
    if sum==n:
        return True
    else:
        return False
    
print(IsSpecialNumber(145))