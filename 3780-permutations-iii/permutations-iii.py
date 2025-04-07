class Solution:
    def permute(self, n: int) -> List[List[int]]:

        result = []

        def backtrack(current, count):
            if n == count:
                result.append(current[:])
                return 
            
            for num in range(1, n+1):
                if num in current:
                    continue
                if current and (current[-1] % 2 == num % 2):
                    continue
                
                current.append(num)
                backtrack(current, count+1)
                current.pop()

        backtrack([], 0)
        return result