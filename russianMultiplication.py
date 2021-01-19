def lenght_justified(l1, l2):
    if len(l1)<len(l2):
        return len(l2)
    return len(l1)

def russianMultiply(a: int, b:int):
    product=0
    left_col=[]
    right_col=[]
    while a>0:
        left_col.append(str(a))
        d=str(b)
        if a&1:
            d+="+"
            product+=b
        right_col.append(d)
        a=a//2
        b=b*2
    return product, left_col, right_col
    
a,left,right=russianMultiply(18,85)
l=lenght_justified(left,right)

for i in range (len(left)):
    print (str(left[i]).rjust(l, " "), str(right[i]).rjust(l, " "))
    
print("==================".rjust(2*l+1," "))
print(str(a).rjust(2*l+1," "))
print("==================".rjust(2*l+1," "))
