# 752. Open the Lock

class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        deadends = set(deadends)
        if "0000" in deadends:
            return -1
        
        v = set(["0000"])
        q = deque([("0000", 0)])
        
        while q:
            c, steps = q.popleft()
            if c == target:
                return steps
            
            for i in range(4):
                for j in [-1, 1]:
                    new_digit = (int(c[i]) + j) % 10
                    new_state = c[:i] + str(new_digit) + c[i+1:]
                    
                    if new_state not in v and new_state not in deadends:
                        v.add(new_state)
                        q.append((new_state, steps + 1))
        
        return -1
