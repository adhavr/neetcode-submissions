class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # if len(s) == 1:
        #     return 1
        hm = {}
        l = 0
        ret = 0
        for r in range(len(s)):
            if s[r] in hm:
                l = max(hm[s[r]] + 1, l)
            hm[s[r]] = r
            ret = max(ret, r-l+1)
        return ret
