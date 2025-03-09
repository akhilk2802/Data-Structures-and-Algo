class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        
        '''
        [0,1,0,0,1,0,1], k = 6
        [0,1,0,0,1,0]

        [0,1,0,0,1,0]
        [0,1,0,0,1,0,1]

        [0,1,0,1,0], k = 3
        [0,1,0,1,0]
        [0,1,0,1,0]
        '''

        n = len(colors)
        l = 0
        result = 0

        for r in range(1, n + k - 1):
            if colors[r % n] == colors[(r - 1) % n]:
                l = r
            if r - l + 1 > k:
                l += 1
            if r - l + 1 == k:
                result += 1

        return result