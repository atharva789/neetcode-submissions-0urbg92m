import numpy as np
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        hashset = set(nums)
        hmap = {}
        longest = float('-inf')
        for val in hashset:
            left = val - 1
            if left not in hashset:
                hmap[val] = [val]
                right = val + 1
                while right in hashset:
                    hmap[val].append(right)
                    right += 1
                longest = len(hmap[val]) if len(hmap[val]) > longest else longest
        return longest
        