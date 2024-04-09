class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return 1
        
        count = {i:0 for i in range(1, n+1)}

        for a, b in trust:
            count[a] -= 1
            count[b] += 1

        print('items: ', count.items())
        for person, score in count.items():
            if score == n-1:
                return person
        
        return -1