class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def is_valid(s):
            balance = 0
            for char in s:
                if char == '(':
                    balance += 1
                else:
                    balance -= 1
                if balance < 0:
                    return False
            return balance == 0
        
        def generate_all(current):
            print("genearted string : ", current)
            if len(current) == 2 * n:
                combinations.append(current)
                return
            generate_all(current + "(")
            generate_all(current + ")")

        combinations = []
        generate_all("")
        return [s for s in combinations if is_valid(s)]
