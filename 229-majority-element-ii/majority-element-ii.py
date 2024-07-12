class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d = {}
        ans = []
        for n in nums:
            if n not in d:
                d[n] = 1
            else:
                d[n] += 1
            
        for num, count in d.items():
            if count > len(nums) // 3:
                ans.append(num)

        return ans
        
        