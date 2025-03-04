class Solution:
    def checkPowersOfThree(self, n: int) -> bool:

        # time and space complexity - 
        # 1. since i am diving n by 3 at every iteration - its going to be O(log3 n) -> this turns out to O(log n)
        # 2. space complexity -> O(1)

        # while n != 1:
        #     # print("n: ", n)
        #     mod = n % 3
        #     if mod > 1:
        #         return False
        #     div = n // 3
        #     if div == 0:
        #         return False
        #     n = div

        # return True

        if n == 1: return True
        if n % 3 > 1: return False
        if n // 3 == 0: return False

        return self.checkPowersOfThree(n // 3)

