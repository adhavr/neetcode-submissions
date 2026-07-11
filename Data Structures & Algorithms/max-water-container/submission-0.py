class Solution:
    def maxArea(self, heights: List[int]) -> int:
        m, l, r = 0, 0, len(heights) - 1
        while l < r:
            height = (r - l) * min(heights[l], heights[r])
            m = max(m, height)
            if heights[l] < heights[r]:
                temp = heights[l]
                while l < r and heights[l] <= temp:
                    l += 1
            else:
                temp = heights[r]
                while l < r and heights[r] <= temp:
                    r -= 1
        return m