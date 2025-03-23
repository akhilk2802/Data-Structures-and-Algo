class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        i = 0
        char_set = set()
        result = 0

        for j in range(len(s)):
            char = s[j]
            while char in char_set:
                char_set.remove(s[i])
                i += 1

            char_set.add(char)
            result = max(result, j - i + 1)

        return result

            
