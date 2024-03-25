# 442. Find All Duplicates in an Array

    def findDuplicates(self, nums):
        ans=list()
        nums.sort()
        n=len(nums)

        for i in range(n-1):
            if nums[i]==nums[i+1]:
                ans.append(nums[i])

        return ans 


        # res = list()
        # for i in nums:
        #     index = abs(i) - 1
        #     if nums[index] < 0:
        #         res.append(abs(i))
        #     else:
        #         nums[index] = -nums[index]
        # return res
