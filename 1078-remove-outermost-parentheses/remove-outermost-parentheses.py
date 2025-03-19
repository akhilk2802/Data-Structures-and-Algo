class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        '''
        i want to understand the question first and then see what i can do right 
        "", "(" + A + ")" 
        1. my questions are, do i have to be worried only about () or {} or any other parantheses 
        2. since you mentioned it is a string, does it only have parantheses or even integers or characters right
        3. wha would be the length of the string 

        usually if there is a string and a parantheses kind of problem, my intuition says its gonna be a stack based problem right 
        correct me if i am wrong
        now lets start with the brute force solution 

        "(()())(())"

        array or something like that 
        since the out put is a string 
        
        ")"

        stack = [(]
        result = "()()()()(())"
        '''
        openP, result = 0, ""
        for char in s:
            if char == ")":
                openP -= 1
            if openP > 0:
                result += char
            if char == "(":
                openP += 1
        return result

        # openP, result = 0, []
        # for char in s:
        #     if char == ")":
        #         openP -= 1
        #     if openP > 0:
        #         result.append(char)
        #     if char == "(":
        #         openP += 1
        # return ''.join(result)