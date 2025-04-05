class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        result = []

        def comb(index, current, total):
            if total == target:
                result.append(current[:])
                return
            if index >= len(candidates) or total > target:
                return 

            current.append(candidates[index])
            comb(index, current, total + candidates[index])
            current.pop()
            comb(index + 1, current, total)

        comb(0, [], 0)
        return result