from typing import List
class Solution:
    # Time complexity - O(n) : single pass throught the array with two pointers
    # Space complexity - O(1) : only tracking two indices with one variable
    def maxProfit(self, prices: List[int]) -> int:
        l, r, maxProfit= 0, 1, 0

        while r<len(prices):
            if prices[r] > prices[l]:
                maxProfit = max(maxProfit, prices[r] - prices[l])
            else:
                l=r
            r+=1
        return maxProfit

# in case of max proift
prices = [7,1,5,3,6,4]
output = Solution()
print("maxProfit", output.maxProfit(prices))

# in case of no profit
prices = [7,6,4,3,1]
print("no maxProfit", output.maxProfit(prices))

