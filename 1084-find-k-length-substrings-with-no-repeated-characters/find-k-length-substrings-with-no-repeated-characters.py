class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        
        # if len(s) < k:
        #     return 0

        # l = 0
        # r = k - 1
        # result = 0


        # while r < len(s):
        #     m = {}
        #     word = s[l:r]

        #     for char in word:
        #         m[char] = m.get(char, 0) + 1

        #     if len(m) == k:
        #         result += 1

        #     l += 1
        #     r += 1

        # return result

        if len(s) < k:
            return 0

        char_count = {}
        result = 0
        l = 0

        for r in range(len(s)):
            char_count[s[r]] = char_count.get(s[r], 0) + 1

            if r - l + 1 > k:
                char_count[s[l]] -= 1
                if char_count[s[l]] == 0:
                    del char_count[s[l]]
                l += 1

            if r - l + 1 == k and len(char_count) == k:
                result += 1

        return result
