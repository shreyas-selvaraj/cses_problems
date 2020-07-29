string = input()
d = {}
counter = 0
final = ""
for char in string:
	if(char not in d):
		d[char] = 1
	else:
		d[char] += 1

for key in d:
	if(d[key] % 2 == 1):
		counter += 1

temp = ""

if(counter > 1):
	print("NO SOLUTION")

elif(counter == 1 and len(string) % 2 == 0):
	print("NO SOLUTION")

elif(len(string) % 2 == 0):
	for key in d:
		final = final + key * (d[key]//2)
	final = final + final[::-1]
	print(final)
else:
	for key in d:
		if(d[key] % 2 == 0):
			final = final + key * (d[key]//2)
		else:
			temp = key * d[key]
	final = final + temp + final[::-1]
	print(final)