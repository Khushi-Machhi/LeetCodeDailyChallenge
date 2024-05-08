# 506. Relative Ranks

class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        indexed_arr = [(score[i], i) for i in range(len(score))]
        sorted_arr = sorted(indexed_arr, key=lambda x: x[0], reverse=True)
    
        ranks = [""] * len(score)
        for i in range(len(sorted_arr)):
            index = sorted_arr[i][1]
            if i == 0:
                ranks[index] = "Gold Medal"
            elif i == 1:
                ranks[index] = "Silver Medal"
            elif i == 2:
                ranks[index] = "Bronze Medal"
            else:
                ranks[index] = str(i + 1)
        
        return ranks
        
