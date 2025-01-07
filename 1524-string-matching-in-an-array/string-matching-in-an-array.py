class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:

        n = len(words)
        result = []
        for i in range(n):
            for j in range(n):
                if words[j] in words[i] and i != j:
                    result.append(words[j])

        return list(set(result))
        