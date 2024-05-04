# 881. Boats to Save People

class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """

        people.sort()
        s, e = 0, len(people) - 1
        boats = 0
        
        while s <= e:
            if people[s] + people[e] <= limit:
                s += 1
            e -= 1
            boats += 1
        
        return boats
        
