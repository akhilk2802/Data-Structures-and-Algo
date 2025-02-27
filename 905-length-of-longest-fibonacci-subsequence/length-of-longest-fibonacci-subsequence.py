class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        
        n = len(arr)
        maxLen = 0
        arrSet = set(arr)

        for start in range(n):
            for next in range(start+1, n):
                prev = arr[next]
                current = arr[start] + arr[next]
                current_len = 2

                while current in arrSet:
                    prev, current = current, current + prev
                    current_len += 1
                    maxLen = max(maxLen, current_len)

        return maxLen