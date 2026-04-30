class Solution:
    def trap(self, height: List[int]) -> int:
        nums = height
        if len(nums) < 3:
            return 0
        left_maxima, right_maxima = [],[]
        l_max, r_max = -1,-1
        for i in range(len(nums)):
            j = len(nums) -1 -i
            l_max, r_max = max(l_max, nums[i]), max(r_max, nums[j])
            left_maxima.append(l_max)
            right_maxima.append(r_max)
        tot = 0
        print(f"left maxima: {left_maxima}")
        print(f"right maxima: {right_maxima}")
        for k in range(len(nums)):
            tot += min(left_maxima[k], right_maxima[-(k+1)]) - nums[k]
        return tot

