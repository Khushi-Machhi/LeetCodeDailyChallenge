#502. IPO

class Solution(object):
    def findMaximizedCapital(self, k, w, profits, capital):
        """
        :type k: int
        :type w: int
        :type profits: List[int]
        :type capital: List[int]
        :rtype: int
        """
        if k == 0:
            return w

        n = len(profits)
        projects = list(zip(capital, profits))
        projects.sort()

        min_capital = []
        max_profit = []

        for project in projects:
            heapq.heappush(min_capital, project)

        curr_capital = w

        for _ in range(k):
           
            while min_capital and min_capital[0][0] <= curr_capital:
                capital_req, profit = heapq.heappop(min_capital)
                heapq.heappush(max_profit, -profit)

            if not max_profit:
                break

            curr_capital += -heapq.heappop(max_profit)

        return curr_capital
