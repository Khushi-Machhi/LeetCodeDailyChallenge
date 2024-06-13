#2037. Minimum Number of Moves to Seat Everyone

class Solution(object):
    def minMovesToSeat(self, seats, students):
        """
        :type seats: List[int]
        :type students: List[int]
        :rtype: int
        """
        seats.sort()
        students.sort()
        
        ans = 0
        n = len(seats)
        for i in range(n):
            ans += abs(seats[i] - students[i])
        
        return ans
    
        
