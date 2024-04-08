# 1700. Number of Students Unable to Eat Lunch

class Solution(object):
    def countStudents(self, students, sandwiches):
        c = students.count(0)
        s = students.count(1)
        
        for i in sandwiches:
            if i == 0:
                if c == 0:
                    break
                else:
                    c -= 1
            else:
                if s == 0:
                    break
                else:
                    s -= 1
        
        return c + s
