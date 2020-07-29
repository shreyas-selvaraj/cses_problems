n = int(input())
ans = []
for i in range(1, n + 1, 2):
	ans.append(i)

for i in range(2, n + 1, 2):
	ans.append(i)

if(n > 1 and n < 4):
	print("NO SOLUTION")
elif(n == 4):
	ans = [2,4,1,3]
	for a in ans:
		print(a, end = ' ')
else:
	for a in ans:
		print(a, end = " ")