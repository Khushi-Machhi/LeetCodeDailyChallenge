#238. Product of Array Except Self

    def productExceptSelf(nums):
        l = len(nums)
        answers = [1]*l
        left_product = 1
        for i in range(l):
            answers[i]*=left_product
            left_product*=nums[i]
        right_product = 1
        for i in range(l-1,-1,-1):
            answers[i]*=right_product
            right_product*=nums[i]
        
        return answers
  productExceptSelf([1,2,3,4,5])
