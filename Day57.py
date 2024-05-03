# 165. Compare Version Numbers

class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = version1.split('.')
        v2 = version2.split('.')
        
        n1, n2 = len(v1), len(v2)
        n = max(n1, n2)
        
        for i in range(n):
            r1 = int(v1[i]) if i < n1 else 0
            r2 = int(v2[i]) if i < n2 else 0
            
            if r1 < r2:
                return -1
            elif r1 > r2:
                return 1
        
        return 0
        
