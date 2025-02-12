class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        
        ans = 0
        prev_max = 0
        for i, x in enumerate(arr):
            prev_max = max(prev_max, x)
            if prev_max == i:
                ans += 1

        return ans