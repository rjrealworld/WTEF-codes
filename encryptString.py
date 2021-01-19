def encrytString(str1):
	s = str1[::-1]
	if 'a' in s:
		s=s.replace('a', '0')
	if 'e' in s:
		s=s.replace('e', '1')
	if 'o' in s:
		s=s.replace('o', '2')
	if 'u' in s:
		s=s.replace('u', '3')
	s=s+'aca'
	return s

s=input()
print(encrytString(s))