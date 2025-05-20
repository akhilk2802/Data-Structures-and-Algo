class Solution:
    def isValid(self, s: str) -> bool:

        if not s:
            return False

        p_map = {
            "(" : ")",
            "{" : "}",
            "[" : "]"
        }

        stack = []

        for ch in s:
            if ch in p_map:
                stack.append(ch)
            elif len(stack) == 0 or p_map[stack.pop()] != ch:
                return False

        return len(stack) == 0