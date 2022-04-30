from random import choice
import collections
class Solution(object):
	def anagrams(self, strs):

		ans = collections.defaultdict(list)

		for s in strs:
			count = [0] * 26

			for c in s:
				count[ord(c) - ord('a')] += 1
			ans[tuple(count)].append(s)
		return ans.values()		

     
	def testcase(self):
		strs = ["eat","tea","tan","ate","nat","bat"]
		print(self.anagrams(strs))   


# Your RandomizedSet object will be instantiated and called as such:
obj = Solution()
obj.testcase()
					