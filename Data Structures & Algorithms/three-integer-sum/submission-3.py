# nums=[-1,0,1,2,-1,-4]
# nums=[-4,-1,-1,0,1,2]

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()
        last_i = -1
        for i,_ in enumerate(nums):
            if i != 0 and nums[i] == nums[last_i]:
                print(f"skipped!!")
                continue
            last_i = i
            k = len(nums) -1
            diff = -nums[i]
            j, k = i+1, len(nums) -1
            last_j = j
            while j < k:
                sum_ = nums[j] + nums[k]
                if sum_ == diff:
                    last_j = j
                    results.append([nums[i],nums[j],nums[k]])
                    while j <= len(nums)-2 and nums[j] == nums[j+1]:
                        # skip to next 
                        j +=1
                    else:
                        j += 1
                    k = len(nums) -1
                elif sum_ < diff:
                    j += 1
                else:
                    k -= 1
        return results
