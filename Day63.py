# 3075. Maximize Happiness of Selected Children

class Solution(object):
    def maximumHappinessSum(self, happiness, k):
        """
        :type happiness: List[int]
        :type k: int
        :rtype: int
        """
        happiness.sort(reverse=True)  
        res = 0
        for i in range(min(len(happiness),k)):
            if happiness[i] <= i:
                break
            res += happiness[i] - i    
        return res


        

