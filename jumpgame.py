

class Solution():
	def uniquepaths(self, m, n):

		if m <= 0 and n <= 0:
			return

		if m == 0 and n == 0:
			return 1

		matrix = [[1 for j in range(n)] for i in range(m)]
		

		for i in range(1,m):
			for j in range(1,n):
				matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]
		return matrix[-1][-1]		

			    
	def testcase(self):
		m = 3
		n = 7
		print(self.uniquepaths(m,n))

obj = Solution()
obj.testcase()