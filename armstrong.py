def convert_into_string(num:int) -> str:
    return str(num)
    
def length_number(n: int) -> int:
    return len(convert_into_string(n))

def digit_power_length(digit:int, length:int) -> int:
    return pow(digit,length)

def sum_digits(num: int) -> int:
    total=0
    for i in convert_into_string(num):
        total+=digit_power_length(int(i),length_number(num))
    return total

def is_armstrong(num:int) -> bool:
    return num==sum_digits(num)
    
a,b=map(int,input().split())
for i in range (a,b+1):
    if is_armstrong(i):
        print (i)
