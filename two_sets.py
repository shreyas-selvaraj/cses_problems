#check if numbers 1...n can be divided into two sets 
#can be divided if total sum is divisible by 2
#if yes, just separate every other digit then put last digit into first array

n = int(input())
set1 = []
set2 = []

# 3 mod 4
if(n % 4 == 0):
	j = 4

else:
	j = 3

if(n * (n+1)/2 % 2 == 0):

	for i in range(0, (n-1)//4): #handle array by fours because 1+4 = 2+3
		set1.append(4 * i + 4 + j)
		set1.append(4 * i + 1 + j)
		set2.append(4 * i + 3 + j)
		set2.append(4 * i + 2 + j)

	if(n % 4 == 0):
		set1.append(4)
		set1.append(1)
		set2.append(3)
		set2.append(2)

	else:
		set1.append(2)
		set1.append(1)
		set2.append(3)	

	print("YES")
	print(len(set1))
	for s in set1:
		print(s, end = ' ')
	print()
	print(len(set2))
	for s in set2:
		print(s, end = ' ')

else:
	print("NO")
