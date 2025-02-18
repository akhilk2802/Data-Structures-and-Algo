class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        
        n = len(s)
        l = 0
        r = n
        perm = []

        for i in range(n+1):
            if i == n:
                if s[i-1] == "I":
                    perm.append(r)
                if s[i-1] == "D":
                    perm.append(l)
                return perm
            if s[i] == "I":
                perm.append(l)
                l += 1
            if s[i] == "D":
                perm.append(r)
                r -= 1
        
        