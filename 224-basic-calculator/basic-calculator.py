class Solution:
    def calculate(self, s: str) -> int:

        stack = []  # Stack to store previous results and signs
        res = 0  # Running result
        num = 0  # Current number
        sign = 1  # +1 for positive, -1 for negative
        
        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)  # Build multi-digit number
            
            elif char in ["+", "-"]:
                res += sign * num  # Apply previous number with its sign
                num = 0  # Reset number
                sign = 1 if char == "+" else -1  # Set sign for next number
            
            elif char == "(":
                # Push current result and sign onto the stack for later use
                stack.append(res)
                stack.append(sign)
                res = 0  # Reset result for inner expression
                sign = 1  # Default sign inside parenthesis
            
            elif char == ")":
                res += sign * num  # Add last number inside parenthesis
                num = 0  # Reset number
                res *= stack.pop()  # Apply saved sign
                res += stack.pop()  # Add saved result from before parenthesis
        
        return res + (sign * num)  # Add last processed number

        