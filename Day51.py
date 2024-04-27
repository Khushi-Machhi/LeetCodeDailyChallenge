# 514. Freedom Trail

class Solution(object):
    def findRotateSteps(self, ring, key):
        m = {}
        
        def dp(ring_i, key_i):
            if key_i == len(key):
                return 0
            
            if (ring_i, key_i) in m:
                return m[(ring_i, key_i)]
            
            c = key[key_i]
            min_steps = float('inf')
            for i in range(len(ring)):
                if ring[i] == c:
                    clock = (i - ring_i) % len(ring)
                    anticlock = (ring_i - i) % len(ring)
                    steps = min(clock, anticlock)
                    next_steps = dp(i, key_i + 1)
                    total_steps = steps + next_steps
                    min_steps = min(min_steps, total_steps)
            
            m[(ring_i, key_i)] = min_steps
            return min_steps
        
        return dp(0, 0) + len(key)  
