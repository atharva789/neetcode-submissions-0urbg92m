class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # two pointer
        i = 0
        j = len(heights) -1
        max_i, max_j, max_area = -1, -1, -1
        while i < j:
            area = min(heights[i], heights[j]) * (j-i)
            if area > max_area:
                max_i = heights[i]
                max_j = heights[j]
                max_area = area
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        return max_area