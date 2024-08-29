from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        sc = Counter(s)
        tc = Counter(t)

        for ch in sc:
            if sc[ch] != tc[ch]:
                return False
        return True