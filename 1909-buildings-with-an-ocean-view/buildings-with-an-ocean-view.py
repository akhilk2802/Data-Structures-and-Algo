class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:

        # algorithm => 
        # initialise a stack with first element of the heights
        # now traverse the array from index 1 to the end
        # check if the stack[-1] is lesser than heights[i]
        # if it is lesser, then pop it, keep doing this comparision until you find a height in stack that is larger than current heights[i]
        # once you find it, stack the current heights[i]
        # return the remaining stack as an output 


        stack = [0]

        for i in range(1, len(heights)):
            while stack and heights[stack[-1]] <= heights[i]:
                    stack.pop()
            stack.append(i)

        
        return stack
