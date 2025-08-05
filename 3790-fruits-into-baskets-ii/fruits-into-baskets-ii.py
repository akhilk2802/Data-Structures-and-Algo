class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:

        res = 0

        for i in range(len(fruits)):
            for j in range(len(baskets)):

                if baskets[j] >= fruits[i] and (baskets[j] != -1 and fruits[i] != -1):
                    print("baskets -> ", baskets[j])
                    print("fruits -> ", fruits[i])
                    res += 1
                    baskets[j] = -1
                    fruits[i] = -1

        return len(fruits) - res