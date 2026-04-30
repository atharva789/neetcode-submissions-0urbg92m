class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        nums = prices
        l,r = 0, 1
        max_profit = 0
        while r < len(nums):
            if nums[r] < nums[l]:
                l = r
                if l == len(nums) -1:
                    r = l
                else:
                    r = l + 1
            else:
                max_profit = max(max_profit, nums[r] - nums[l])
                r += 1
        return max(0, max_profit)