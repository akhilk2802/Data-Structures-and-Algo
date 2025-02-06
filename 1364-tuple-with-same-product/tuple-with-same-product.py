class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:

        m = {}
        n = len(nums)
        total = 0

        for i in range(n):
            for j in range(i+1, n):
                val = nums[i] * nums[j]

                if val in m:
                    m[val] += 1
                else:
                    m[val] = 1

        print("Map : ", m)

        for _, val in m.items():
            pairs = ((val - 1) * val//2)
            total += 8 * pairs

        return total