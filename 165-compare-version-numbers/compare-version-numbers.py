class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:

        split_v1 = version1.split(".")
        a1 = list(map(int, split_v1))

        split_v2 = version2.split(".")
        a2 = list(map(int, split_v2))

        len_v1 = len(split_v1)
        len_v2 = len(split_v2)

        maxlen = max(len_v1, len_v2)
        a1.extend([0] * (maxlen - len_v1))
        a2.extend([0] * (maxlen - len_v2))

        for i in range(maxlen):
            if a1[i] > a2[i]:
                return 1
            elif a1[i] < a2[i]:
                return -1

        return 0