class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        def helper(st):
            stack = []
            for char in st:
                if char == "#":
                    if len(stack) > 0:
                        stack.pop()
                else:
                    stack.append(char)
            
            return "".join(stack)
        
        finS = helper(s)
        finT = helper(t)

        return finS == finT

