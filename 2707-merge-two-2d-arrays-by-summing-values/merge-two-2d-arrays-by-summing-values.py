class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:

        m = {}

        for i, j in nums1:
            m[i] = j

        for i, j in nums2:
            if i in m:
                m[i] += j
            else:
                m[i] = j

        sorted_m = dict(sorted(m.items()))
        result = []

        for i, j in sorted_m.items():
            result.append([i, j])
        return result

        
        