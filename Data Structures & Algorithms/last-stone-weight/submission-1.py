class Solution:
    import heapq
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] *= -1
        heapq.heapify(stones)
        while len(stones) > 1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)
            if x < y:
                heapq.heappush(stones, x-y)
            elif y > x:
                heapq.heappush(stones, y-x)
        if len(stones) == 1:
            return stones[0]*-1
        return 0