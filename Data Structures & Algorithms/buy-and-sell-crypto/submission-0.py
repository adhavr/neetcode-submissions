class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m = 0
        i = 0
        j = 1
        while j < len(prices) and i <= j:
            if prices[j] < prices[i]:
                i = j
                j += 1
            elif prices[j] - prices[i] > m:
                m = prices[j] - prices[i]
                j += 1
            else:
                j += 1
            print(i, j, m)
        return m