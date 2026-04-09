class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        hashset = set()
        for val in nums:
            if val in hashset:
                continue
            hashset.add(val)
        seq_starts = {}
        largest_seq = float('-inf')
        for val in hashset:
            if val-1 not in hashset:
                seq_starts[val] = []
        for val in hashset:
            smallest_delta = float('inf')
            for start_num in seq_starts:
                delta = val - start_num
                if delta < smallest_delta:
                    smallest_delta = delta
            key = val - smallest_delta
            seq_starts[key].append(val)
            largest_seq = len(seq_starts[key]) if len(seq_starts[key]) > largest_seq else largest_seq
        if largest_seq == float('-inf'):
            return 1
        return int(largest_seq)+1
        