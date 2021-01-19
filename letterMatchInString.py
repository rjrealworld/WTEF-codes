def letterMathch(str1, str2):
    if len(str1)<len(str2):
        n= len(str1) 
    else:
        n= len(str2)
    
    count=0
    for i in range (n):
        if str1[i]==str2[i]:
            count+=1
    return count


str1, str2=input().split()
print(letterMathch(str1, str2))