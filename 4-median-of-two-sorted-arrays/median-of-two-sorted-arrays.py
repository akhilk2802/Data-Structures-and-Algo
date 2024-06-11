class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i, j = 0, 0
        final = []

        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                final.append(nums1[i])
                i += 1
            else:
                final.append(nums2[j])
                j += 1
        while i < len(nums1):
            final.append(nums1[i])
            i += 1
        while j < len(nums2):
            final.append(nums2[j])
            j += 1

        mid = len(final) // 2
 
        if len(final) % 2 == 0:
            return (final[mid] + final[mid - 1])/2
        else:
            return final[mid]