class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        nums = prices
        l,r = 0, 1
        max_profit = 0
        while r < len(nums):
            if nums[l] < nums[r]:
                max_profit = max(max_profit, nums[r] - nums[l])
            else:
                l = r
            r += 1
        return max(0, max_profit)