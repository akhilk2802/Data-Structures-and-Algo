class Solution:
    def totalFruit(self, fruits: List[int]) -> int:

        if len(fruits) <= 2:
            return len(fruits)

        len_fruits = len(fruits)

        m = {}
        l = 0
        r = 0
        res = 0

        for r in range(len(fruits)):
            m[fruits[r]] = m.get(fruits[r], 0) + 1

            while len(m) > 2:
                m[fruits[l]] -= 1
                if m[fruits[l]] == 0:
                    del m[fruits[l]]
                l += 1

            res = max(res, r - l + 1)
            
        return res