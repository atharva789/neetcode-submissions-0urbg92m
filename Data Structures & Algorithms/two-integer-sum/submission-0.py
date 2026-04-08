class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = set()
        for i in range(len(nums)):
            if nums[i] in seen:
                return [nums.index(target - nums[i]), i]
            difference = target - nums[i]
            seen.add(difference)
            