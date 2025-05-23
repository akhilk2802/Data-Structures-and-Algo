class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        char_set = set()
        count = 0
        l = 0

        for r in range(len(s)):

            while s[r] in char_set:
                char_set.remove(s[l])
                l+=1

            char_set.add(s[r])
            count = max(count, r - l + 1)

        return count

