import matplotlib.pyplot as plt
import string

def countAlphaFreq(file_name: string) -> {str : int} :
    freqs={}
    for letter in string.ascii_lowercase:
        freqs[letter] = 0
        
    with open(file_name, encoding="utf8") as f:
        for line in f:
            for char in line.lower():
                if char in freqs:
                    freqs[char] += 1
                elif char in string.ascii_lowercase:
                    freqs[char] = 1
    return freqs

freqs = countAlphaFreq('WarAndPeace.txt')
plt.grid(axis = 'y')
plt.xlabel('Alphabet')
plt.ylabel('Frequency')
plt.bar(freqs.keys(), freqs.values())
plt.show()
