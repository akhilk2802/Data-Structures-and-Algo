class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()
        result = []

        def comb(current, i, total):
            if total == target:
                result.append(current[:])
                return
            if i >= len(candidates) or total > target:
                return 

            current.append(candidates[i])
            comb(current, i + 1, total + candidates[i])
            current.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            
            comb(current, i + 1, total)
        
        comb([], 0, 0)

        return result