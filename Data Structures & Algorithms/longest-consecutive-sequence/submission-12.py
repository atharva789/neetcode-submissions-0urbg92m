import numpy as np
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        longest = 0
        for n in nums:
            if (n - 1) not in hashset:
                length = 0
                while (n + length) in hashset:
                    length += 1
                longest = max(length, longest)    
        return longest
        