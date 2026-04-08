class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        prod = 1
        prefix_arr = [1 for _ in range(size)]
        suffix_arr = [1 for _ in range(size)]
        for i in range(size):
            # compute prefixes
            prefix_idx, suffix_idx = i, size -1 -i
            prefix =1
            suffix = 1
            prefix_num, suffix_num = 1,1
            if prefix_idx != 0:
                prefix = prefix_arr[prefix_idx-1]
                prefix_num = nums[prefix_idx-1]
            prefix_prod = prefix * prefix_num
            prefix_arr[prefix_idx] = prefix_prod
            # compute suffixes
            if suffix_idx < size -1:
                suffix = suffix_arr[suffix_idx + 1]
                suffix_num = nums[suffix_idx + 1]
            suffix_prod = suffix * suffix_num
            suffix_arr[suffix_idx] = suffix_prod
        # compute products: use prefix_arr as the final products array
        print(f"PREFIXES: {prefix_arr}")
        print(f"SUFFIXES: {suffix_arr}")
        for i, num in enumerate(prefix_arr):
            prefix_arr[i] = num * suffix_arr[i]
        return prefix_arr

        