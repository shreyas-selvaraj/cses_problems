import math 
def canEmpty(a,b):
	if((a + b) % 3 == 0 and 2 * a >= b and 2 * b >= a): #the 2*a stuff is for keeping one half of the other because its take 1 and 2
		return "YES"
	else:
		return "NO"

T = int(input())
ans = []

for i in range(T):
	arr = [int(x) for x in input().split(" ")]
	ans.append(canEmpty(arr[0], arr[1]))

for a in ans:
	print(a)