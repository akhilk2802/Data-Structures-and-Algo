class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        '''
        checklist ->
        1. remove the min number of parantheses, either ( or ) - any position
        2. is valid if -
            1. empty string, lower case characters
            2. (A) -> enclosed between the parantheses
            3. two valid strings concatenated
        '''

        result = []
        count = 0

        for i in range(len(s)):
            if s[i] == "(":
                count += 1
            if s[i] == ")" and count > 0:
                result.append(s[i])
                count -= 1
            elif s[i] != ")":
                result.append(s[i])

        filtered = []
        for c in result[::-1]:
            if c == "(" and count > 0:
                count -= 1
            else:
                filtered.append(c)

        return "".join(filtered[::-1])