# 3068. Find the Maximum Sum of Node Values

class Solution(object):
    def maximumValueSum(self, nums, k, edges):
        """
        :type nums: List[int]
        :type k: int
        :type edges: List[List[int]]
        :rtype: int
        """

        xor = [(num^k)-num for num in nums]
        xor.sort()
        xor.reverse()
        possibleMaxSum = sum(nums)

        for i in range(0,len(nums)-1,2):
            path = xor[i]+xor[i+1]
            if path<=0:
                break
            possibleMaxSum+=path

        return possibleMaxSum

        # possibleMaxSum = 0

        # for i in nums:
        #     xor = i ^ k
        #     possibleMaxSum += max(i , xor)

        # return possibleMaxSum

        # xorArr = [number ^ k for number in nums]
        # possibleMaxSum = 0
        # n = len(nums)

        # for i in range(n):
        #     possibleMaxSum += max(nums[i],xorArr[i])

        # return possibleMaxSum

       


        
