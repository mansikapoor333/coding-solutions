class Solution(object):
	def numIsland(self, prices):

		minprice = float('inf')
		maxprofit= 0

		for price in prices:
			if price < minprice:
				minprice = price

			if price - minprice > maxprofit:
				maxprofit = price - minprice

		return maxprofit		
				

	

	def testcase(self):
		prices = [7,1,5,3,6,4]
		print(self.numIsland(prices))



obj = Solution()
obj.testcase()			