class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:

        n = len(words)
        words.sort(key=len)
        result = set()
        for i in range(n):
            for j in range(i+1, n):
                if words[i] in words[j]:
                    result.add(words[i])

        return list(result)
        