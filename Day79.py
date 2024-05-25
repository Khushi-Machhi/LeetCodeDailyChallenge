#140. Word Break II
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        word_set = set(wordDict)
        memo = {}

        def dfs(start):
            if start in memo:
                return memo[start]
            
            if start == len(s):
                return ['']

            sentences = []
            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word in word_set:
                    rest_of_sentences = dfs(end)
                    for sentence in rest_of_sentences:
                        if sentence:
                            sentences.append(word + ' ' + sentence)
                        else:
                            sentences.append(word)
            
            memo[start] = sentences
            return sentences

        word_set = set(wordDict)
        memo = {}

        def dfs(start):
            if start in memo:
                return memo[start]
            
            if start == len(s):
                return ['']

            sentences = []
            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word in word_set:
                    rest_of_sentences = dfs(end)
                    for sentence in rest_of_sentences:
                        if sentence:
                            sentences.append(word + ' ' + sentence)
                        else:
                            sentences.append(word)
            
            memo[start] = sentences
            return sentences

        return dfs(0)
        
