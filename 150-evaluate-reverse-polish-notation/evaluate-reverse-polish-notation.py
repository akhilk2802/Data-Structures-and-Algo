class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if not tokens:
            return None

        stack = []
        o = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: b - a,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(b/a)
        }

        for token in tokens:
            try:
                num = int(token)
                stack.append(num)
            except:
                a = stack.pop()
                b = stack.pop()
                stack.append(o[token](a, b))
        return stack.pop()
        