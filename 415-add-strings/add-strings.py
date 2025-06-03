class Solution:
    def addStrings(self, num1: str, num2: str) -> str:

        i, j = len(num1) - 1, len(num2) - 1
        carry = 0
        result = []

        while i >= 0 or j >= 0 or carry:
            in1 = int(num1[i]) if i >= 0 else 0
            in2 = int(num2[j]) if j >= 0 else 0

            _sum = in1 + in2 + carry
            carry = _sum // 10
            result.append(str(_sum % 10))

            i -= 1
            j -= 1

        print("result -> ", result)
        return "".join(result[::-1])