class Solution:
    def isValid(self, word: str) -> bool:

        vowels = {'a', 'i', 'e', 'o', 'u'}

        vowel_count = 0
        consonant_count = 0

        if len(word) < 3:
            return False
        
        for ch in word: 
            ch = ch.lower()
            if ch.isalnum():
                if ch.isalpha() and ch in vowels:
                    vowel_count += 1
                if ch.isalpha() and ch not in vowels:
                    consonant_count += 1
            else:
                return False
                
        if vowel_count >= 1 and consonant_count >= 1:
            return True

        return False


        