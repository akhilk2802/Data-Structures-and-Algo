class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        '''
        1234   100    200

        put all the elements in the nums to set called s
        now i go to each of the element 
        traverse until i find the element less than the current element by 1 in the s
        if it is not present move on to next element 
        if it is present, keep looking and updating the count by 1 until the condition holds

        '''
        count = 0 
        num_set = set(nums)

        for num in num_set:
            if (num - 1) not in num_set:
                length = 1
                while (num + length) in num_set:
                    length += 1
                count = max(count, length)

        return count