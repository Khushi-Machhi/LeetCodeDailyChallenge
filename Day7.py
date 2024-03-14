# 930. Binary Subarrays With Sum

 def numSubarraysWithSum(nums, goal):
        c = 0
        s = 0
        s_freq = {0: 1}  
        for i in nums:
            s += i
            if (s - goal) in s_freq:
                c += s_freq[s - goal]
            s_freq[s] = s_freq.get(s, 0) + 1
        return c   
    # def numSubarraysWithSum(self, nums, goal):
    #     c, s = 0, 0
    #     l = len(nums)
    #     for j in range(l):
    #         s = 0  
    #         for i in range(j, l):
    #             s += nums[i]
    #             if goal == s:
    #                 c += 1
    #             elif s > goal:  
    #                 break
    #     return c

    # def numSubarraysWithSum(self, nums, goal):
    #     count = 0
    #     prefix_sum_freq = {0: 1} 
    #     prefix_sum = 0
    #     for num in nums:
    #         prefix_sum += num
    #         if prefix_sum - goal in prefix_sum_freq:
    #             count += prefix_sum_freq[prefix_sum - goal]
    #         prefix_sum_freq[prefix_sum] = prefix_sum_freq.get(prefix_sum, 0) + 1

    #     return count
numSubarraysWithSum([1,0,1,0,1],2)
