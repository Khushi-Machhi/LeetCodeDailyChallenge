#1122. Relative Sort Array

class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        rank = {val: index for index, val in enumerate(arr2)}
        
        def sortkey(x):
           
            if x in rank:
                return (0, rank[x])
            else:
                return (1, x)
        
        arr1.sort(key=sortkey)
        
        return arr1
        
