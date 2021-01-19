def convert_into_lower(array:[str]) -> [str]:
    return [i.lower() for i in array] 

def element_sorted_array(array: [str]) -> [str]:
   return [''.join(sorted(array[i].lower())) for i in range (len(array))]

def groupAnagrams(words: [str]) -> [str]:
    dupArray=element_sorted_array(words)

    word_taken=[]
    anagram_together=[]

    for i in range(len(dupArray)):
        if dupArray[i] not in word_taken:
            word_taken.append(dupArray[i])
            together=[]
            for j in range (i, len(dupArray)):
                if dupArray[i]==dupArray[j]:
                    together.append(words[j])
            anagram_together.append(together)
    return anagram_together
          
words = list(map(str,input().split()))
print(groupAnagrams(words))