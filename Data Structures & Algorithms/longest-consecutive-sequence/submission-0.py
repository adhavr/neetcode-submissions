class Solution:
    from collections import defaultdict
    def longestConsecutive(self, nums: List[int]) -> int:
        hm = defaultdict(int)
        m = 0
        for num in nums:
            if not hm[num]:
                hm[num] = hm[num-1] + hm[num+1] + 1
                hm[num - hm[num-1]] = hm[num]
                hm[num + hm[num+1]] = hm[num]
                m = max(m, hm[num])
        return m
        