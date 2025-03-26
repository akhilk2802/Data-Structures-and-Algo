class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        '''
        k = 2
        friends = 3
        '''

        friends = [i for i in range(1, n + 1)]
        start = 0
        
        while len(friends) > 1:
            removal = (start + k - 1) % len(friends)
            friends.pop(removal)
            start = removal
        
        return friends[0]
