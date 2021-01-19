word="AAABBBBCCDD" 
ans=""
i=0
while (i<len(word)):
    count=1
    for j in range (i+1,len(word)):
        if word[i] == word [j]:
            count+=1
        else:
            break
    if count > 2:
        ans+=str(count)+word[i]
    else:
        ans+=word[i]*count
    i=j
print(ans)
    