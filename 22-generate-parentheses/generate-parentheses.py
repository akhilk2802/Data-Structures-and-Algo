class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        def backtrack(open_len, close_len, current):

            if len(current) == 2 * n:
                result.append(current)

            if open_len > close_len:
                backtrack(open_len, close_len + 1, current + ")")
            
            if open_len < n:
                backtrack(open_len + 1, close_len, current + "(")


        result = []
        backtrack(0, 0, "")
        return result