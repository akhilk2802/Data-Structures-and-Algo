class Solution:
    def checkPowersOfThree(self, n: int) -> bool:


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