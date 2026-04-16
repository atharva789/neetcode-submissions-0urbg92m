# nums=[-4,-1,-1,0,1,2]
# hashmap = {
    # -4: 1,
    # -1:2,
    # 0:1, 
    # 1:1,
    # 2:1
#}
class Solution:
    def get_two_pointer_soln(self, nums: List[int]) -> list[List[int]]:
        results = []
        nums.sort()
        last_i = -1
        for i,_ in enumerate(nums):
            if nums[i] > 0:
                break
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

    def get_hmap_soln(self, nums: List[int]) -> List[List[nums]]:
        results = []
        nums.sort()
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        
        for i in range(len(nums)):
            count[nums[i]] -= 1

            if i and nums[i] == nums[i -1]:
                continue
            
            for j in range(i+1, len(nums)):
                count[nums[j]] -= 1
                if j -1 > i and nums[j] == nums[j-1]:
                    continue
                target = -(nums[i]+nums[j])
                if count[target] > 0:
                    results.append([nums[i], nums[j], target])
            for j in range(i+1, len(nums)):
                count[nums[j]] += 1
        return results


    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = self.get_hmap_soln(nums)
        return results
