class Solution:
    def calculate(self, s: str) -> int:

        '''
        s -> expression with digits and signs, NO Parantheses
        Evalute and return value -> integer
        given expression -> valid
        BODMAS

        Example ->
        Input -> 3 + 2 * 2
        Output -> 3 + 4 -> 7

        Example 2 -> 
        Input -> 3 / 2
        Output -> 1

        Example 3 ->
        Input -> 3 + 5 / 2
        Output -> 3 + 2 -> 5
        '''

        '''
        Approach ->
        1. Use a Stack
        2. Iterate through the given expression
        3. Every time we find theres an expression

        3 + 2 * 2
        '''
        stack = []

        num = 0
        sign = "+"

        for i, char in enumerate(s):

            if char.isdigit():
                num = num * 10 + int(char)

            if char in "+-/*" or i == len(s) - 1:
                if sign == "+":
                    stack.append(num)
                if sign == "-":
                    stack.append(-num)
                if sign == "/":
                    stack.append(int(stack.pop() / num))
                if sign == "*":
                    stack.append(stack.pop() * num)
                
                num = 0
                sign = char

        return sum(stack)