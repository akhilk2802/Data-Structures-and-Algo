class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        '''
        [1,1,2,3,4,5]
         l     x r
        '''

        left, right = 0, len(arr) - 1

        while left <= right and (right - left + 1) > k:
            if abs(x - arr[left]) > abs(arr[right] - x):
                left += 1
            else:
                right -= 1

        result = arr[left:right+1]
        return result