#count for k 1 - n, how many ways knights can be placed on board so that they don't attack each other 
def num_ways(n):
	#try every starting place on board 
	#for every starting place, add number of squares remaining that second knight can be placed 
	#have to take combination not permutation
	if(n == 1):
		return 0
	if(n == 2):
		return 6
	num_squares = n * n
	num_ways = 0
	total_comb = num_squares * (num_squares - 1)//2 #total ways to place two knights 
	#subtract from total
	first_row = 4 * n 
	second_row = 4 * (n-2)
	besides_two_rows = num_squares - first_row - second_row
	total_comb = total_comb - besides_two_rows * 8 // 2 - first_row * 4 // 2 - second_row * 6 // 2
	return total_comb

n = int(input())
ans = []

for i in range(1, n + 1):
	ans.append(num_ways(i))

for a in ans:
	print(a)