class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:

        # Algo - 
        # 1. Generate all the posibilities
        # 2. Keep Checking if the generated string is in the nums
        # 3. If its not there, go to next 
        # 4. Return the first generated string which is not in nums

        n = len(nums)
        b_set = set(nums)
        s = {"0", "1"}

        def gen(s, n, current = ""):
            if len(current) == n:
                if current not in b_set:
                    return current
                return None

            for c in s:
                result = gen(s, n, current + c)
                if result:
                    return result
            return None
        
        
        return gen(s, n)

        
