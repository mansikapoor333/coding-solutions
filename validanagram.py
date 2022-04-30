from random import choice
import collections
class Solution(object):
	def validanagrams(self, s, t):

		dict_={}

		for i in s:
			if i in dict_:
				dict_[i] += 1
			else:
				dict_[i] = 1

		for i in t:
			if i in dict_:
				dict_[i] -= 1
			else:
				dict_[i] = 1

		for k in dict_:
			if dict_[k] != 0:
				return False
		return True		
				
     
	def testcase(self):
		s = "anagram"
		t = "nagaram"
		print(self.validanagrams(s,t))   


# Your RandomizedSet object will be instantiated and called as such:
obj = Solution()
obj.testcase()
					