class Solution:
    def clearDigits(self, s: str) -> str:

        stack = []
        for ch in s:
            stack.append(ch)

            if ch.isdigit() and len(stack):
                stack.pop()
                stack.pop()
            
        print("stack : ", stack)
        return "".join(stack)
            
        