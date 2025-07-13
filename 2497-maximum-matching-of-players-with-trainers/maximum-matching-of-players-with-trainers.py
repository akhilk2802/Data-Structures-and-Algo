class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:

        '''

        players => [4, 7, 9]
        trainers => [8, 2, 5, 8]

        players => [4, 7, 9]
        trainers => [2, 5, 8, 8]

        '''

        players.sort()
        trainers.sort()

        count = 0

        i = 0
        j = 0

        while (i < len(players) and j < len(trainers)) :
            if (players[i] <= trainers[j]):
                count += 1
                i += 1
                j += 1
            else:
                j += 1

        return count
