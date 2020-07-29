N = input()
arr = [int(x) for x in input().split(" ")]

cmax = 0
ans = 0
for i in range(len(arr)):
	cmax = max(cmax, arr[i])
	ans += cmax - arr[i]

print(ans)