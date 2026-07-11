class Solution:
    from collections import defaultdict
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        t_maps = Counter(t)
        s_maps = Counter()
        best = ""
        l = 0
        r = 0

        while r < len(s):
            s_maps[s[r]] += 1
            while all(s_maps[ch] >= t_maps[ch] for ch in t_maps):
                if best == "" or (r - l + 1) < len(best):
                    best = s[l:r+1]
                s_maps[s[l]] -= 1
                l += 1
            r += 1
        return best