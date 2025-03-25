class Solution:
    def kthGrammar(self, n: int, k: int) -> int:

        # Optimal ->
        cur = 0
        left = 0
        right = 2 ** (n-1)

        for _ in range(n-1):
            mid = (left + right) // 2
            if k <= mid:
                right = mid
            else:
                left = mid + 1
                cur = 0 if cur else 1

        return cur


        


        # start = "0"
        # for i in range(1, n):
        #     new = ""
        #     for c in start:
        #         if c == "0":
        #             new += "01"
        #         if c == "1":
        #             new += "10"
        #     start = new
        # return int(start[k-1])

        # Brute Force Solution ->
        # arr = ["0"] * n

        # for i in range(1, n):
        #     prev = arr[i-1]
        #     new = ""
        #     for c in prev:
        #         if c == "0":
        #             new += "01"
        #         if c == "1":
        #             new += "10"
        #     arr[i] = new

        # return int(arr[n-1][k-1])




