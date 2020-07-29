def trailing_zeroes(N):
	#only need to check how many tens there are
	counter = 0
	i = 5
	ans = 0
	while(i <= N):
		ans += N//i
		i = i * 5
		
	return ans

n = int(input())
print(trailing_zeroes(n))