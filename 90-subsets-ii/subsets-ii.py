class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        def subset(input, output, result = []):

            if len(input) == 0:
                result.append(output)
                return 
            
            subset(input[1:], output + [input[0]], result)
            subset(input[1:], output, result)

        nums.sort()
        result = []
        subset(nums, [], result)
        return list(map(list, set(map(tuple, result))))
        