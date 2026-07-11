class Solution:
    from collections import defaultdict
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = defaultdict(list)
        for word in strs:
            hm1 = [0] * 26
            for ch in word:
                hm1[ord(ch)-97] += 1
            hm[str(hm1)].append(word)
        return list(hm.values())