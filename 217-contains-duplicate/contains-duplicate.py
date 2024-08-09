from collections import Counter
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        counts = Counter(nums)
        for key, val in counts.items():
            if val >= 2:
                return True
            
        return False
