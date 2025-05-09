class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        m = {}

        for c in strs:
            sorted_c = "".join(sorted(c))

            if sorted_c not in m:
                m[sorted_c] = [c]
            else:
                m[sorted_c].append(c)

        # print("m : ", m)
        return [v for v in m.values()]