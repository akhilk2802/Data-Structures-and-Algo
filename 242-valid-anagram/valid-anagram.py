class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sSort = sorted(s)
        tSort = sorted(t)

        return sSort == tSort