class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        s_pointer, t_pointer = 0, 0
    
    # Loop until we've checked all characters in s or t
        while s_pointer < len(s) and t_pointer < len(t):
        # If characters match, move to the next character in s
            if s[s_pointer] == t[t_pointer]:
                s_pointer += 1
        
        # Always move to the next character in t
            t_pointer += 1
    
    # If we've gone through all characters in s, it's a subsequence
        return s_pointer == len(s)
