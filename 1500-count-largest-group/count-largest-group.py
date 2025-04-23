class Solution:
    def countLargestGroup(self, n: int) -> int:
        
        def findSum(x):
            total = 0
            x = abs(x)
            while x > 0:
                total += x % 10
                x //= 10
            return total
        
        m = {}

        for i in range(1, n + 1):

            t = findSum(i)
            if t in m:
                m[t].append(i)
            else:
                m[t] = [i]

        max_size = max(len(v) for v in m.values())
        count = 0
        for v in m.values():
            if len(v) == max_size:
                count += 1

        return count