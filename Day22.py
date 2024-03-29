# 2962. Count Subarrays Where Max Element Appears at Least K Times

    def countSubarrays(self, nums, k):
        m = max(nums)
        c,l = 0,0
        s = {}
    
        for right, num in enumerate(nums):
            s[num] = s.get(num, 0) + 1

            while m in s and s[m] >= k:
                c += len(nums) - right
                s[nums[l]] -= 1
                if s[nums[l]] == 0:
                    del s[nums[l]]
                l += 1

        return c
