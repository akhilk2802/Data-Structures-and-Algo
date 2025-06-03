class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:

        s = set(arr)
        i = 1

        while k > 0:

            if i in s:
                i += 1
            else:
                k -= 1
                if k == 0:
                    return i
                i += 1
