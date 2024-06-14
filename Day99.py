# 945. Minimum Increment to Make Array Unique

class Solution(object):
    def minIncrementForUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort() 
        res = 0
        n = len(nums) 
        for i in range(1, n):
            if nums[i] <= nums[i - 1]:
                inc = nums[i - 1] - nums[i] + 1
                nums[i] += inc
                res += inc
        
        return res
