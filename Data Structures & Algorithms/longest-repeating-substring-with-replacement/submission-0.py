class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hm = {}
        l = 0
        maxf = 0
        ret = 0
        for r in range(len(s)):
            hm[s[r]] = hm.get(s[r], 0) + 1
            maxf = max(maxf, hm[s[r]])
            while k + maxf < r - l + 1:
                hm[s[l]] -= 1
                l += 1
            ret = max(ret, r-l+1)
        return ret