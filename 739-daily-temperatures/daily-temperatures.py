class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        n = len(temp)
        stack = []
        result = [0] * n

        for i, value in enumerate(temp):
            while stack and value > stack[-1][1]:
                stackInd, stackValue  = stack.pop()
                result[stackInd] = i - stackInd
            stack.append((i, value))
        return result