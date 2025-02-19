class Solution:
    def partition(self, s: str) -> List[List[str]]:

        # Algo - 
        # generate a substring using recursion
        # generate a substring and check if it is a valid palindrome
        # if it is then add it to the result array
        
        def isPalindrome(subString):
            l, r = 0, len(subString)-1
            while l <= r:
                if subString[l] == subString[r]:
                    l += 1
                    r -= 1
                else:
                    return False
            return True
        
        def generateSubString(start, path, result, s):
            if start == len(s):
                result.append(path[:])

            for end in range(start + 1, len(s) + 1):
                sub = s[start:end]
                if isPalindrome(sub):
                    path.append(sub)
                    generateSubString(end, path, result, s)
                    path.pop()

        result = []
        generateSubString(0, [], result, s)
        return result
