class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:

        # [1,3,5]
        #    ^
        count = 0
        MOD = 10 ** 9 + 7
        prefixSum = 0
        oddCount = 0
        evenCount = 1

        for num in arr:
            prefixSum += num
            if prefixSum % 2 == 0:
                count += oddCount
                evenCount += 1
            else:
                count += evenCount
                oddCount += 1

            count %= MOD

        return count
