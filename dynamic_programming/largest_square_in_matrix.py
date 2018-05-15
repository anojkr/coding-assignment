#https://www.geeksforgeeks.org/maxaimum-size-sub-matrix-with-all-1s-in-a-binary-matrix/

def largest_square_in_matrix(matrix):
	n = len(matrix)
	for i in range(1,n):
		for j in range(1,len(matrix[i])):
			if matrix[i][j] is 1:
				matrix[i][j] = 1 + min(matrix[i-1][j-1],matrix[i-1][j],matrix[i][j-1])
			elif matrix[i][j] is 0:
				matrix[i][j] = 0
	[print(k) for k  in matrix]

M = [[0, 1, 1, 0, 1],
    [1, 1, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0]]

largest_square_in_matrix(M)