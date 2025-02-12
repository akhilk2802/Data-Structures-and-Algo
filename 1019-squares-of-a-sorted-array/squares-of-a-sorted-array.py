class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        ans = []
        for n in nums:
            ans.append(n*n)

        return sorted(ans)
        