class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        nums = numbers
        for i in range(len(nums)):
            l,r = i + 1, len(nums) -1
            diff = target - nums[i]
            while l <= r:
                mid = l + (r - l)//2
                if nums[mid] == diff:
                    return [i+1, mid+1]
                elif nums[mid] < diff:
                    l = mid + 1
                else:
                    r = mid - 1
        return []