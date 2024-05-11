# 857. Minimum Cost to Hire K Workers

class Solution(object):
    def mincostToHireWorkers(self, quality, wage, k):
        """
        :type quality: List[int]
        :type wage: List[int]
        :type k: int
        :rtype: float
        """
        n = len(quality)
        w = sorted((float(wage[i]) / quality[i], quality[i]) for i in range(n))
        cost = float('inf')
        sum_q = 0
        max_h = []
        
        for ratio, q in w:
            heapq.heappush(max_h, -q)
            sum_q += q
            
            if len(max_h) > k:
                sum_q += heapq.heappop(max_h)
                
            if len(max_h) == k:
                cost = min(cost, ratio * sum_q)
                
        return cost

        
        
