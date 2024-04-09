# 2073. Time Needed to Buy Tickets

class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        n = len(tickets)
        c = 0
        while tickets[k] > 0:
            for i in range(n):
                if tickets[i] > 0:
                    tickets[i] -= 1
                    c += 1
                    if i == k and tickets[i] == 0:
                        return c
        return c
