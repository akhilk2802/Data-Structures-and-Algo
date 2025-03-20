class Solution:
    def firstUniqChar(self, s: str) -> int:

        m = Counter(s)

        for i, char in enumerate(s):
            if m[char] == 1:
                return i

        return -1
        
        