class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        # If the matrix is empty, return an empty list.
        if not matrix or not matrix[0]:
            return []
        
        result = []
        # Define the boundaries of the matrix.
        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1

        # Loop until the boundaries cross.
        while left <= right and top <= bottom:
            # Traverse from left to right along the top row.
            for col in range(left, right + 1):
                result.append(matrix[top][col])
            top += 1  # Move the top boundary down.

            # Traverse from top to bottom along the right column.
            for row in range(top, bottom + 1):
                result.append(matrix[row][right])
            right -= 1  # Move the right boundary to the left.

            # If there are still rows remaining, traverse the bottom row from right to left.
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    result.append(matrix[bottom][col])
                bottom -= 1  # Move the bottom boundary up.

            # If there are still columns remaining, traverse the left column from bottom to top.
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    result.append(matrix[row][left])
                left += 1  # Move the left boundary to the right.

        return result

        