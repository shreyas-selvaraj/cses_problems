# https://fishi.devtail.io/weblog/2015/05/18/common-bitwise-techniques-subset-iterations/
def divide(n, arr):
	#find sum closest to s/2 --> return s-2*ans
	# if current sum <= s/2 then ans = max of current sum and ans 
	#for each length of subset calculate sum for subsets 

	msk = 0;
	ans = 0
	s = 0
	for i in range(len(arr)):
		s += arr[i]

	for msk in range (0, 1 << n): #creates binary mask to subset over 
		cs = 0
		for j in range(0, n):
			if((msk >> j) & 1): # get nth bit past mask 
				cs += arr[j] 
		if(cs <= s/2):
			ans = max(ans, cs)

	return(s - 2 * ans)

N = int(input())
arr = [int(x) for x in input().split(" ")]
print(divide(N, arr))