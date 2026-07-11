class MedianFinder:
    import heapq
    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        if self.small and num <= self.small[0]*-1:
            heapq.heappush(self.small, num*-1)
        else:
            heapq.heappush(self.large, num)
        
        if len(self.small)-1 > len(self.large):
            heapq.heappush(self.large, -1*heapq.heappop(self.small))
        if len(self.large)-1 > len(self.small):
            heapq.heappush(self.small, -1*heapq.heappop(self.large))

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return self.small[0]*-1
        elif len(self.large) > len(self.small):
            return self.large[0]
        return (self.large[0]+self.small[0]*-1)/2
        