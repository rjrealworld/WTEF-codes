CHANGE_BY=13

def encrypt(s):
    i=0
    encrypted=''
    for i in s:
        if ord (i) in range (65, 78) or ord(i) in range (97, 110):
            encrypted += chr(ord(i) + CHANGE_BY)
        elif ord (i) in range (78, 91) or ord (i) in range (110, 123):
            encrypted += chr(ord(i) - CHANGE_BY)
        else:
            encrypted += i
    return encrypted

print(encrypt('this is a sentence')) 