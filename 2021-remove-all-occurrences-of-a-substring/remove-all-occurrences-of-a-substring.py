class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:

        stack = []
        pl = len(part)

        for ch in s:
            stack.append(ch)

            if len(s) >= pl and "".join(stack[-pl:]) == part:
                del stack[-pl:]

        return "".join(stack)