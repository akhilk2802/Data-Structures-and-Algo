class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        newStr = ""

        for i in range(len(s)):

            if s[i].isalnum():
                newStr += s[i].lower()

        print("newStr : ", newStr)
        return newStr == newStr[::-1]