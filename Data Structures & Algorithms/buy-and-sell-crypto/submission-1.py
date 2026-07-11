class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m = 0
        i = 0
        j = 1
        while j < len(prices) and i <= j:
            if prices[j] < prices[i]:
                i = j
            m = max(m, prices[j] - prices[i])
            j += 1
        return m