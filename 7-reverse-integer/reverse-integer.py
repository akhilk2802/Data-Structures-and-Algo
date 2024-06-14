class Solution:
    def reverse(self, x: int) -> int:

        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        # Handle the sign of the number
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        # Reverse the digits
        reversed_x = 0
        while x != 0:
            pop = x % 10
            x //= 10
            # Check for overflow before updating reversed_x
            if (reversed_x > INT_MAX // 10) or (reversed_x == INT_MAX // 10 and pop > 7):
                return 0  # It would overflow
            reversed_x = reversed_x * 10 + pop
        
        return sign * reversed_x
        