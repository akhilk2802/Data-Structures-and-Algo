class Solution:
    def largestOddNumber(self, num: str) -> str:
        
        '''
        brute force approach -> 
        write a function to check if the given str is odd or even

        create a number of possible substrings 

        questions from me -> 
        will it be possible for the string to start from "0 to 6" in example 2 ?
        something like -> "06" 
        
        considering yes it does 
        lets create number of possible substrings
        so how do i create possiblities now ? 
        i can use a 2 for loop, something like two pointers and keep creating the possible substrings

        4206
         ^
           ^ 
        '''
        # n = len(num)
        # maxVal = -1

        def isOdd(s):
            n = int(s)
            if n % 2 == 0:
                return False
            return True

        # for i in range(n):
        #     for j in range(i, n):
        #         if isOdd(num[i:j+1]):
        #             maxVal = max(maxVal, int(num[i:j+1]))

        # if maxVal == -1:
        #     return ""

        # return str(maxVal)

        '''
        now lets optimise this problem right, currently the time complexity is O(n^2)
        i can reduce it -> 
        i just saw the hint lol, now lets go and implement it right
        '''
        n = len(num)
        for i in range(n-1, -1, -1):
            if isOdd(int(num[i])):
                return num[:i+1]

        return ""