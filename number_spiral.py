def calculate(i, j):
	ans = 0
	z = max(i, j) #separates columns and rows into increasing starting and ending with even numbers 
	z2 = (z-1) * (z-1)
	if z % 2 == 0:
		#make formula for value based on column and row 
		if j == z: #column wise 
			ans = z2 + i
		else: #going across row 
			ans = z2 + i + z - j
	else:
		if i == z:
			ans = z2 + j
		else:
			ans = z2 + j + z - i
	return ans

	

T = int(input())
ans = []

for i in range(T):
	arr = [int(x) for x in input().split(" ")]
	ans.append(calculate(arr[0], arr[1]))

for a in ans:
	print(a)