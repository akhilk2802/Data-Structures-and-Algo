class Solution:
    def calPoints(self, operations: List[str]) -> int:

        score_stack = []

        for char in operations:
            if char.lstrip('-').isdigit():
                score_stack.append(int(char))
            if char == "C":
                score_stack.pop()
            if char == "D":
                prev = score_stack[-1]
                score_stack.append(2 * prev)
            if char == "+":
                prev1 = score_stack[-1]
                prev2 = score_stack[-2]
                score_stack.append(prev1 + prev2)
            # print("Stack -> ", score_stack)

        return sum(score_stack)
        