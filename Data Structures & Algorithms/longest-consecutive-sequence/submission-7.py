import numpy as np
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
            check = val -1
            if check not in hashset:
                seq_starts[val] = [val]
        print(f"[DEBUG] sequence starters: {seq_starts}")
        for val in hashset:
            if val in seq_starts:
                continue
            else:
                smallest_delta = {
                    "sign": None,
                    "val":float('inf')
                    }
                for start_num in seq_starts:
                    delta = val - start_num
                    if abs(delta) < smallest_delta['val']:
                        smallest_delta['val'] = abs(delta)
                        smallest_delta['sign'] = int(-1 *np.sign(delta))
                print(f"[DEBUG] {smallest_delta}")
                key = val + int(smallest_delta['sign'])*smallest_delta['val']
                print(f"[DEBUG] VAL={val} assigned --> KEY={key}")
                seq_starts[int(key)].append(val)
                largest_seq = len(seq_starts[key]) if len(seq_starts[key]) > largest_seq else largest_seq
        if largest_seq == float('-inf'):
            return 1
        print(f"[DEBUG] {seq_starts}")
        return largest_seq
        