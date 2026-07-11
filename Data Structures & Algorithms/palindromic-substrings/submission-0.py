class Solution:
    def countPalindromes(self, s, l, r):
        ret = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            ret += 1
            l -= 1
            r += 1
        return ret

    def countSubstrings(self, s: str) -> int:
        ret = 0
        for i in range(len(s)):
            ret += self.countPalindromes(s, i, i)
            ret += self.countPalindromes(s, i, i+1)
        return ret
