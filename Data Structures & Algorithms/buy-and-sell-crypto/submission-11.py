class Solution:
    def twoPointerSolution(self, nums: List[int]) -> int:
        l,r = 0, 1
        max_profit = 0
        while r < len(nums):
            if nums[l] < nums[r]:
                max_profit = max(max_profit, nums[r] - nums[l])
            else:
                l = r
            r += 1
        return max(0, max_profit)
    
    def dpSolution(self, nums: List[int]) -> int:
        minBuy = nums[0]
        maxP = 0
        for price in nums:
            minBuy = min(price, minBuy)
            maxP = max(maxP, price - minBuy)
        return maxP

    def maxProfit(self, prices: List[int]) -> int:
        return self.dpSolution(prices)
