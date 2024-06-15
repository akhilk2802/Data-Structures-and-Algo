class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {"(" : ")", "{" : "}", "[" : "]"}

        if s is None:
            return False

        for i in s:
            if i in d:
                stack.append(i)
            elif len(stack) == 0 or d[stack.pop()] != i:
                return False

        return len(stack) == 0

        