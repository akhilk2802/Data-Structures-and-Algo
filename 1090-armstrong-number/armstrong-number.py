class Solution:
    def isArmstrong(self, n: int) -> bool:

        digits = str(n)
        num_digits = len(digits)
        armstrong_sum = sum(int(digit) ** num_digits for digit in digits)

        return armstrong_sum == n