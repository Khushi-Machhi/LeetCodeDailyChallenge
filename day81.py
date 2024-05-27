# 1608. Special Array With X Elements Greater Than or Equal X

class Solution(object):
    def specialArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums.sort(reverse=True)
        for x in range(1, len(nums) + 1):
            if nums[x-1] >= x and (x == len(nums) or nums[x] < x):
                return x
        return -1
        
