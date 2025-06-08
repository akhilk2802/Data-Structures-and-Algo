class Solution:
    def validPalindrome(self, s: str) -> bool:

        '''
        should i worry about lowercase / upper ?
        no 
        lowercase
        length of the string ?
        integers in the sting ?
        '''

        left, right = 0, len(s) - 1
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                substr1 = s[left+1 : right+1]
                substr2 = s[left: right]
                return substr1 == substr1[::-1] or substr2 == substr2[::-1]

        return True