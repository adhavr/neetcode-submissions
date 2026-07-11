class Solution:
    from collections import defaultdict
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums) + 1)]
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        for item in count.items():
            print(item)
            buckets[item[1]].append(item[0])
        ret = []
        i = len(buckets) - 1
        while len(ret) < k:
            ret = ret + buckets[i]
            i -= 1
        return ret[:k]
        