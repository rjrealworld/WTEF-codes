def findTrailingZeros(n): 
	five_multiples = 0
	i=5
	while (n/i>=1): 
		five_multiples += int(n/i) 
		i *= 5
	return five_multiples
n = 6
print(findTrailingZeros(n)) 
