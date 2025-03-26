class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:

        stack = []
        pl = len(part)

        for ch in s:
            stack.append(ch)

            if len(stack) >= pl and "".join(stack[-pl:]) == part:
                del stack[-pl:]

        return "".join(stack)