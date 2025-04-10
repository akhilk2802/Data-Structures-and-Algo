class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        wordSet = set(wordDict)
        memo = {}

        def backtrack(start):

            if start in memo:
                return memo[start]

            
            if start == len(s):
                return [""]

            result = []

            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word in wordSet:
                    sub_sentences = backtrack(end)
                    for sub in sub_sentences:
                        result.append(word + (" " + sub if sub else ""))
            
            memo[start] = result
            return result
        
        return backtrack(0)