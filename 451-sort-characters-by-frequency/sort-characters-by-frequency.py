class Solution:
    def frequencySort(self, s: str) -> str:

        m = {}
        for ch in s:
            if ch in m:
                m[ch] += 1
            else:
                m[ch] = 1

        sorted_m = dict(sorted(m.items(), key=lambda item: item[1], reverse=True))
        result = ""

        for k, v in sorted_m.items():
            print("value : ", k*v)
            result += (k*v)

        return result