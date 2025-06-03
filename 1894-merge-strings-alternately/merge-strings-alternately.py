class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        m = ""
        l1 = len(word1)
        l2 = len(word2)
        i, j = 0, 0

        while i < l1 and j < l2:
            m += word1[i]
            m += word2[j]
            i +=1 
            j += 1

        while i <l1:
            m += word1[i]
            i += 1
        
        while j < l2:
            m += word2[j]
            j += 1

        return m