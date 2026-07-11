class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ret = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            ret[i] *= prefix
            prefix *= nums[i]
        prefix = 1
        i = len(nums) - 1
        while i >= 0:
            ret[i] *= prefix
            prefix *= nums[i]
            i -= 1
        return ret