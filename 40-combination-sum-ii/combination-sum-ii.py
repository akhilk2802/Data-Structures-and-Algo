class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()
        result = []

        def backtrack(current, pos, target):
            if target == 0:
                result.append(current[:])
            if target <= 0:
                return

            prev = -1
            for i in range(pos, len(candidates)):
                if candidates[i] == prev:
                    continue
                current.append(candidates[i])
                backtrack(current, i + 1, target - candidates[i])
                current.pop()
                prev = candidates[i]
            
        backtrack([], 0, target)
        return result
