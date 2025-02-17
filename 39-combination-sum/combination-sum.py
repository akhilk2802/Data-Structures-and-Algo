class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        result = []
        current = []

        def comb(ind, target):

            if len(candidates) == ind:
                if target == 0:
                    result.append(current[:])
                return

            if candidates[ind] <= target:
                current.append(candidates[ind])
                comb(ind, target-candidates[ind])
                current.pop()
            comb(ind+1, target)

        comb(0, target)
        return result