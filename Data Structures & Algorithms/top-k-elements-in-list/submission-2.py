import math

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # bucket sort?
        min_val, max_val = min(nums), max(nums)
        if max_val == min_val:
            return [max_val]
        n = len(nums)
        buckets = [[[], 0] for _ in nums]
        for num in nums:
            idx = math.floor(((num - min_val)/(max_val-min_val)) * (n-1))
            while len(buckets[idx][0]) > 0 and num != buckets[idx][0][-1]: # if not the same as the last element
                # if next bucket has the same element
                if idx + 1 <= len(buckets) -1:
                    idx += 1
                else:
                    buckets.insert(idx + 1, [[num], 0])
                    continue
            buckets[idx][0].append(num)
            buckets[idx][1] +=1
        # sort tuples
        print(buckets)
        buckets = sorted(buckets, key=lambda x: x[1])
        result, filtered = [], buckets[-k:]
        for res in filtered:
            result.append(res[0][0])
        return result
        
