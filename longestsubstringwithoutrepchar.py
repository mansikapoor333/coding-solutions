

class Solution():
	def longestsubstring(self, s):
		i = j = 0
		chars = set()
		maxlength = 0

		while (i < len(s) and j < len(s)):

			if s[j] not in chars:
				chars.add(s[j])
				j += 1
				maxlength = max(maxlength, j-i)
				

			else:
				chars.remove(s[i])
				i += 1

		return maxlength		

					

	def testcase(self):
		s = "abcabcbb"
		print(self.longestsubstring(s))

obj = Solution()
obj.testcase()

		

        # return maxlength 