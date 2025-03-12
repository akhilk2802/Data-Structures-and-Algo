class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        

        '''
        brute force =>
        use hashmap , return the one with only one element 

        optimised => 
        binary search =>
        [1,1,2,3,3,4,4,8,8]
        [0,1,2,3,4,5,6,7,9]

        [3,3,7,7,10,11,11]
        [0,1,2,3,4 ,5 ,6 ]

        if all the elements are in pairs from the start
        find the mid, if the mid is odd and the second element is on odd we know the element is on the left
        else the element is on the right 
        now based on this observation we can manipulate the low and high of the search algorithm
        '''

        l, r = 0, len(nums) - 1

        while l < r:

            mid = (l + r) // 2
            
            if mid % 2 == 1:
                mid -= 1
            if nums[mid] != nums[mid + 1]:
                r = mid
            else:
                l = mid + 2

        return nums[l]