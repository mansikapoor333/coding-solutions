class Solution(object):
	def twosum(self, nums, target):
		dict_={}

		for i in range(len(nums)):
			if nums[i] not in dict_:
				dict_[target-nums[i]] = i

			else:
				return [dict_[nums[i]],i]


	def testcase(self):
		nums = [2,7,11,15]
		target = 9
		print(self.twosum(nums,target))

obj = Solution()
obj.testcase()		
				
				