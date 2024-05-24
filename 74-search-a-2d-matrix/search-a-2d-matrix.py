class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
            
        rows, cols = len(matrix), len(matrix[0])
        low, high = 0, (rows * cols - 1)
    
        while(low <= high):

            mid = (low + high)//2
            
            row = mid // cols
            col = mid % cols
            
            if(matrix[row][col] == target): return True
            elif(target > matrix[row][col]): low = mid + 1
            else: high = mid - 1

        return False
        