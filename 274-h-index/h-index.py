class Solution:
    def hIndex(self, citations: List[int]) -> int:

        citations = sorted(citations, reverse=True)
        print(citations)
        h = 0

        n = len(citations)

        for i in range(n):
            if citations[i] >= i + 1:
                h = i+1
            else:
                break
            
        return h
        