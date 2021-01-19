def is_Palindrome (num: int) -> bool :
    string1=str(num)
    string2=str(num)[::-1]
    if string1==string2:
        return True
    return False

def doubleBasePalindrome(n: int):
    if is_Palindrome(n):
        binary=bin(n)[2:]
        if is_Palindrome(int(binary)):
            return True
    return False


print(doubleBasePalindrome(int(input())))