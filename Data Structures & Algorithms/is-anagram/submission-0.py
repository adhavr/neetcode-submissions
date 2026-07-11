class Solution:
    from collections import defaultdict
    def isAnagram(self, s: str, t: str) -> bool:
        hm = defaultdict(int)
        for ch in s:
            hm[ch] += 1
        for ch in t:
            if ch not in hm:
                return False
            hm[ch] -= 1
            if hm[ch] == 0:
                hm.pop(ch)
        if len(hm) == 0:
            return True
        return False