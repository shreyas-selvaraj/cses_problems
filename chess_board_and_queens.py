#The input has eight lines, and each of them has eight characters. Each square is either free (.) or reserved (*).
#how many ways to place queens such that they are not attacking 
#find all ways then subtract ones that have a queen on a nonfree square?
#numbered 1 2 3 4 5... horizontally 
board = []
bad_squares = []
total = 0
for i in range(8):
	board.append(input().split(" "))

for i in range(len(board)):
	for j in range(len(board[i])):
		if(board[i][j] == "*"):
			bad_squares.append((i) * 8 + j + 1)

b = {}
for i in range(1, 65):
	if(i in bad_squares):
		b[i] = False
	else:
		b[i] = True

i = 1
while(i <= 8):
	if(b[i] not in bad_squares):
		
	else:
		i += 1