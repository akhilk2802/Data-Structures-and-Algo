class Solution:
    def minSwaps(self, data: List[int]) -> int:
        
        c1 = sum(data)
        if c1 <= 1:
            return 0

        current_ones = sum(data[:c1])
        print("current ones : ", data[:c1])
        max_ones = current_ones

        for i in range(c1, len(data)):
            current_ones += data[i] - data[i - c1]
            max_ones = max(max_ones, current_ones)

        print("C1 : ", c1)

        return c1 - max_ones