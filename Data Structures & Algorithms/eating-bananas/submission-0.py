class Solution:
    import math
    def isEatable(self, piles, h, k):
        total = 0
        for pile in piles:
            total += math.ceil(pile / k)
            if total > h:
                return False
        return True
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        r = max(piles)
        l = 1
        res = r
        while r >= l:
            mid = (l+r) // 2
            total = 0
            for pile in piles:
                total += math.ceil(pile / mid)
            if total <= h:
                r = mid - 1
                res = mid
            else:
                l = mid + 1
        return res