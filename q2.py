def convert_string(a: int) -> str:
    return str(a)

def sort_list(n: int) -> [str]:
    return sorted(convert_string(n))
    
def reverse(l:[str]) -> [str]:
    return l[::-1]
    
def largest(n: int) -> str:
    return ''.join(reverse(sort_list(n)))
    
def smallest(n:int) -> str:
    return ''.join(sort_list(n))

def difference(n: int) -> int:
    return int(largest(n))-int(smallest(n))

def fun(n: int) -> int:
    diff1=difference(n)
    diff2=difference(diff1)
    while (diff1!=diff2):
        diff1=diff2
        diff2=difference(diff2)
    return diff2
    
n=int(input())
print(fun(n))
