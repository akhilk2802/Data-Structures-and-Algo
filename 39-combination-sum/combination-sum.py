class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        result = []
        ans = []
       
        def backtrack(ind, target):
            if ind == len(candidates):
                if target == 0:
                    ans.append(result[:])
                return 
            if candidates[ind] <= target:
                result.append(candidates[ind])
                backtrack(ind, target - candidates[ind])
                result.pop()
            backtrack(ind + 1, target)

            
        backtrack(0, target)
        return ans
    
            
            
            
