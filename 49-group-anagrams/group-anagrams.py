class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        m = {}

        for c in strs:
            sorted_c = "".join(sorted(c))

            # m.get(sorted_c, []).append(c)

            if sorted_c in m:
                m[sorted_c].append(c)
            else:
                m[sorted_c] = [c]

        # print("map : ", m)
        return [c for c in m.values()]