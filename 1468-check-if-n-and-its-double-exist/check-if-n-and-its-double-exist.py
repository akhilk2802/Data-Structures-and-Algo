class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:

        eSet = set()
        for num in arr:
            if 2 * num in eSet or (num % 2 == 0 and num // 2 in eSet):
                return True
            eSet.add(num)
        return False