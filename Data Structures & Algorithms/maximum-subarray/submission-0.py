class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s = 0
        m = nums[0]
        for n in nums:
            s += n
            m = max(m, s)
            if s < 0:
                s = 0
        return m