

class Solution():
	def JumpGame(self, nums):

		destination = len(nums)-1
		source = destination - 1


		while source >= 0:
			if source + nums[source] >= destination:
				destination = source
				source -= 1

			else:
				source -= 1

		return True if destination == 0 else False		
			    
	def testcase(self):
		nums = [2,3,1,1,4]
		print(self.JumpGame(nums))

obj = Solution()
obj.testcase()