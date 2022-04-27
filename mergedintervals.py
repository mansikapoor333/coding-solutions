class Solution(object):
	def mergeintervals(self, intervals):

		intervals.sort(key=lambda x: x[0])

		merged = []

		for interval in intervals:
			if not merged or merged[-1][1] < interval[0]:
				merged.append(interval)
			else:
				merged[-1][1] = max(merged[-1][1], interval[1])

		return merged		
				

	def testcase(self):
		intervals = [[1,4],[4,5]]
		print(self.mergeintervals(intervals))

obj = Solution()
obj.testcase()			