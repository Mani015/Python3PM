
# 1 st 10 number divisible by 7

a = 0
i = 1

# while a<10:
#     if i%7==0:
#         print('divisible by 7:',i)
#         a = a + 1
#
#     i = i + 1
#
# print('loop excuted compelte')


# for i in range(71):
#     if i%7==0:
#         print(i)
#

# Usage: python3 addMatricesCLIFile.py mat1.txt mat2.txt mat3.txt
'''

import sys

def getMatrix(filename):
	fileObj = open(filename)
	Matrix = []
	while True:
		line = fileObj.readline()
		if len(line) == 0: break
		row = line.split()
		row = [int(n) for n in row]
		Matrix.append(row)
	fileObj.close()
	return Matrix

def getOrder(mat):
	r = len(mat)
	c = len(mat[0])
	return r, c

def addMatrices(A, B, r, c):
	Matrix = []
	i = 0
	while i < r:
		j = 0
		row = []
		while j < c:
			data = A[i][j] + B[i][j]
			row.append(data)
			j = j + 1
		Matrix.append(row)
		i = i + 1
	return Matrix

def writeMatrix(filename, mat):
	fileObj = open(filename, 'w')
	r, c = getOrder(mat)
	i = 0
	while i < r:
		line = ' '.join([str(x) for x in mat[i]]) # line = ' '.join(['5', '5', '5']) '5 5 5'
		fileObj.write(line + '\n')
		i = i + 1
	fileObj.close()


#main app begins here
n = len(sys.argv)
if n != 4:
	print('I need 3 files through CLI')
	sys.exit(1)

Mat1 = getMatrix(sys.argv[1])
#print(Mat1)
Mat2 = getMatrix(sys.argv[2])
#print(Mat2)
r1, c1 = getOrder(Mat1)
r2, c2 = getOrder(Mat2)
if r1 != r2 or c1 != c2:
	print('addition is not possible... Matrices order is not same')
	sys.exit(1)

Mat3 = addMatrices(Mat1, Mat2, r1, c1)
#print(Mat3)
# writeMatrix(sys.argv[3], Mat3)