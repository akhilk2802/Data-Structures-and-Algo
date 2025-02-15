class Solution:
    def punishmentNumber(self, n: int) -> int:
        def isValid(num: str, target: int, curr_sum: int, index: int) -> bool:
            if index == len(num):
                return curr_sum == target
            
            for j in range(index, len(num)):
                part = int(num[index:j+1])
                if isValid(num, target, curr_sum + part, j + 1):
                    return True
            
            return False

        total_sum = 0
        for i in range(1, n + 1):
            squared_str = str(i * i)
            if isValid(squared_str, i, 0, 0):
                total_sum += i * i
        
        return total_sum