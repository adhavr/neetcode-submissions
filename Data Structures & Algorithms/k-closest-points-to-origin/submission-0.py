class Solution:
    import heapq
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        for i in range(len(points)):
            points[i] = (math.sqrt(points[i][0]*points[i][0] + points[i][1]*points[i][1]), points[i])
        heapq.heapify(points)
        ret = []
        while k > 0:
            ret.append(heapq.heappop(points)[1])
            k-=1
        return ret