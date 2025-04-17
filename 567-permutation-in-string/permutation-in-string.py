class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        s1_sorted = "".join(sorted(s1))
        n, m = len(s1), len(s2)

        for i in range(m - n + 1):
            if ''.join(sorted(s2[i : i + n])) == s1_sorted:
                return True
        return False

        

        # win_size = len(s1)
        # s1_m = Counter(s1)
        # n = len(s2)

        # s2_m = {}
        # l = 0

        # for r in range(n):
        #     s2_m[s2[r]] = 1 + s2_m.get(s2[r], 0)
        #     while len(s2_m) > win_size:
        #         s2_m[s2[l]] -= 1
        #         if s2_m[s2[l]] == 0:
        #             del s2_m[s2[l]]
        #         l += 1
        #     if s1_m == s2_m:
        #         return True
        # return False

        # s1 = s1.sort()
        # s2_len = len(s2)
        # s1_len = len(s1)

        # for i in range(s2_len - s1_len):
        #     window = s2[i:i + s1_len]
        #     if s1 == window.sort()