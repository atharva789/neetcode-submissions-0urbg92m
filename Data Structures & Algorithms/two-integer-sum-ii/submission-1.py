class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        nums = numbers
        i = 0
        j = len(nums) -(i+1)
        while i < j:
            diff = target - nums[i]
            if diff == nums[j]:
                break
            elif diff > nums[j]:
                i += 1
            else:
                j -= 1

        print(f"[DEBUG] {nums[i]} + {nums[j]} = {nums[i] + nums[j]}")
        return [i+1,j+1]