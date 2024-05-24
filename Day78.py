# 1255. Maximum Score Words Formed by Letters

class Solution(object):
    def maxScoreWords(self, words, letters, score):
        """
        :type words: List[str]
        :type letters: List[str]
        :type score: List[int]
        :rtype: int
        """

        def wordScore(word):
            return sum(score[ord(char) - ord('a')] for char in word)
        
        def canform(word, letter_count):
            word_count = Counter(word)
            for char, cnt in word_count.items():
                if letter_count[char] < cnt:
                    return False
            return True
        
        def dfs(index, current_score, letter_count):
            if index == len(words):
                return current_score
            
            max_score = dfs(index + 1, current_score, letter_count)
            
            word = words[index]
            if canform(word, letter_count):
                new_letter_count = letter_count.copy()
                for char in word:
                    new_letter_count[char] -= 1
                max_score = max(max_score, dfs(index + 1, current_score + word_scores[index], new_letter_count))
            
            return max_score
        
        word_scores = [wordScore(word) for word in words]
        letter_count = Counter(letters)
        
        return dfs(0, 0, letter_count)
        
