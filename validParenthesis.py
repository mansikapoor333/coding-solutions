class Solution(object):
	def valid(self, s):

		dict_ = {')':'(', '}':'{', ']':'['}
		stack = []

		for char in s:
			if char in dict_.values():
				stack.append(char)

			elif char in dict_.keys():
				if stack == [] or dict_[char] != stack.pop():
					return False

			else:
				return False

		return stack == []
					
				









	
				

	

	def testcase(self):
		s = "()"
		print(self.valid(s))



obj = Solution()
obj.testcase()			