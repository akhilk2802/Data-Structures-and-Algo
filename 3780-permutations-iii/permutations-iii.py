class Solution:
    def permute(self, n: int) -> List[List[int]]:

        '''
        brute force approach -> create all the permutations and them check for the validity with the give condition and the add it to the result 

        for n = 4
        i need to deal with 1, 2, 3, 4

        for n = 3 -> 
        1,2,3
        1,3,2
        2,3,1
        2,1,3
        3,1,2
        3,2,1
        '''

        result = []
        
        def backtrack(current, count):
            if count == n:
                result.append(current[:])
                return 
            
            for num in range(1, n + 1):
                if num not in current and (not current or current[-1] % 2 != num % 2):
                    current.append(num)
                    backtrack(current, count + 1)
                    current.pop()
            
        backtrack([], 0)
        return result
