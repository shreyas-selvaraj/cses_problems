string = input()
c = 0
curr = 'A'
ret = 1
for char in string:
	if(char == curr):
		c += 1
		ret = max(ret, c)

	else:
		curr = char
		c = 1

print(ret)