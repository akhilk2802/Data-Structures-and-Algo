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
        count = 0 # count of number of open parantheses

        for char in s:
            if char == "(":
                count += 1
            if char == ")" and count > 0:
                result.append(char)
                count -= 1
            elif char != ")":
                result.append(char)


        filtered = []
        for char in result[::-1]:
            if char == "(" and count > 0:
                count -= 1
            else:
                filtered.append(char)

        return "".join(filtered[::-1])