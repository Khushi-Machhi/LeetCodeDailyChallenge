# 2958. Length of Longest Subarray With at Most K Frequency

    def maxSubarrayLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        n=len(nums)
        start,end=0,0
        max_length=0
        freq={}
        while end<n:
            freq[nums[end]]=freq.get(nums[end],0)+1
            while freq[nums[end]]>k:
                freq[nums[start]]-=1
                start+=1
            max_length=max(max_length,end-start+1)
            end+=1  
        return max_length 


        # freq = {}
        # max_length = 0
        # l = 0
        
        # for r in range(len(nums)):
        #     freq[nums[r]] = freq.get(nums[r], 0) + 1
            
        #     while max(freq.values()) > k:
        #         freq[nums[l]] -= 1
        #         if freq[nums[l]] == 0:
        #             del freq[nums[l]]
        #         l += 1
            
        #     max_length = max(max_length, r - l + 1)
        
        # return max_length
