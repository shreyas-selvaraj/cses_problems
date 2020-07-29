from itertools import permutations 

string = input()
string = sorted(string)
final = ""
for element in string:
	final += element
s = set([''.join(p) for p in permutations(final)])
print(len(s))
for e in s:
	print(e)