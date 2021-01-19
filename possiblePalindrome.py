def is_palindrome(s: str) -> bool :
    return s == s[::-1]

def check_odd_frequency (frequencies) -> bool :
    count=0
    for i in frequencies.values():
        if i % 2 == 1:
            count += 1
            if count > 1:
                return False
    return True

def get_letters_frequency (string : str) :
    count_letters = {}
    for letter in set(string):
        count_letters [letter] = string.count(letter)
    return count_letters

def is_possible_palindrome(word: str) -> bool :
    if is_palindrome (word):
        return True
    freq = get_letters_frequency (word)
    return check_odd_frequency ( freq )    

print(is_possible_palindrome(input()))