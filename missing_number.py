N = input()
arr = [int(x) for x in input().split(" ")]
s = 0
for i in range(len(arr)):
	s += arr[i]

print(N*(N+1)//2 - s)