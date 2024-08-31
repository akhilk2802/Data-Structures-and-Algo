from collections import Counter 
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        r_counter = Counter(ransomNote)
        m_counter = Counter(magazine)

        if r_counter & m_counter == r_counter:
            return True
        return False
               