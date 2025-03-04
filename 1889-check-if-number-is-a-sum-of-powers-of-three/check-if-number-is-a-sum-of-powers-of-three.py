class Solution:
    def checkPowersOfThree(self, n: int) -> bool:

        # Algorithm - 
        # will be using modulo 
        # every number will be use a modulo to get either 0 or 1 
        # will have to use modulo and division both 

        print("n before: ", n)

        while n != 1:
            # print("n: ", n)
            mod = n % 3
            if mod > 1:
                return False
            
            div = n // 3
            if div == 0:
                return False
            
            n = div

        return True
            