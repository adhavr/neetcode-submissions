class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        minVal = nums[0]

        while r >= l:
            mid = (l + r) // 2

            if nums[mid] >= minVal:
                l = mid + 1
            else:
                minVal = nums[mid]
                r = mid - 1
        return minVal