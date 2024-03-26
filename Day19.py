# 41. First Missing Positive
class Solution(object):
    def firstMissingPositive(self, nums):
        n = len(nums)
        i = 0
        while i < n:
            if 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
            else:
                i += 1
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        return n + 1
