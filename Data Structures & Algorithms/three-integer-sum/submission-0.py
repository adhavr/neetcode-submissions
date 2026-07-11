class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ret = []
        for i in range(len(nums)-1):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] + nums[i] > 0:
                    r -= 1
                elif nums[l] + nums[r] + nums[i] == 0:
                    ret.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l-1] == nums[l] and l < r:
                        l += 1
                else:
                    l += 1
        return ret