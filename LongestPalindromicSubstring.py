# from random import choice
# import collections
# from collections import deque
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        resLen = 0
        
        #odd length
        for i in range(len(s)):
            l,r = i,i
            while l>=0 and r <len(s) and s[l] == s[r]:
                if (r-l+1) > resLen:
                    res = s[l:r+1]
                    resLen = r-l+1
                l = l-1
                r = r+1
            #even length    
            l,r = i,i+1
            while l>=0 and r <len(s) and s[l] == s[r]:
                if (r-l+1) > resLen:
                    res = s[l:r+1]
                    resLen = r-l+1
                l = l-1
                r = r+1
        return res
    def testcase(self):
    	s = "babad"
    	print(self.longestPalindrome(s))   
     	# print(self.getHits(300)) 

obj = Solution()
obj.testcase()
# obj.hit(timestamp)
# obj.getHits(timestamp)
					