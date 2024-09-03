def is_integer(s):
    if not s:
        return False
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()
    
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        if not tokens:
            return None
        
        stack = []
        n = len(tokens)

        for i in range(n):
            if is_integer(tokens[i]):
                stack.append(int(tokens[i]))
            elif tokens[i] in "+/*-":
                a = stack.pop()
                b = stack.pop()
                if tokens[i] == "+":
                    c = a+b
                    stack.append(c)
                if tokens[i] == "-":
                    c = b-a
                    stack.append(c)
                if tokens[i] == "*":
                    c = a*b
                    stack.append(c)
                if tokens[i] == "/":
                    c = int(b/a)
                    stack.append(c)        
        return stack.pop()