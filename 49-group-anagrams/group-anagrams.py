class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        m = {}

        for s in strs:
            sortString = "".join(sorted(s))

            if sortString not in m:
                m[sortString] = []

            m[sortString].append(s)
        
        print("map : ", m)
        return list(m.values())
        