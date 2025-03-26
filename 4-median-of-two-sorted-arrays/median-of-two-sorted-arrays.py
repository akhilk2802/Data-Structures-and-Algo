class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        
        combined = nums1 + nums2
        combined.sort()

        n = len(combined)

        if n % 2 == 1:
            return combined[n // 2]
        else:
            return (combined[n // 2 - 1] + combined[n // 2]) / 2.0

        
        # n1 = len(nums1)
        # n2 = len(nums2)
        # n3 = n1 + n2

        # ind2 = n3 // 2
        # ind1 = ind2 - 1
        # count, ind1el, ind2el = 0, -1, -1

        # i, j = 0, 0
        # while i < n1 and j < n2:
        #     if nums1[i] < nums2[j]:
        #         if count == ind1:
        #             ind1el = nums1[i]
        #         if count == ind2:
        #             ind2el = nums1[i]
        #         count += 1
        #         i += 1
        #     else:
        #         if count == ind1:
        #             ind1el = nums2[j]
        #         if count == ind2:
        #             ind2el = nums2[j]
        #         count += 1
        #         j += 1

        # # Process remaining elements in nums1 (if nums2 is exhausted)
        # while i < n1:
        #     if count == ind1:
        #         ind1el = nums1[i]
        #     if count == ind2:
        #         ind2el = nums1[i]
        #     count += 1
        #     i += 1

        # # Process remaining elements in nums2 (if nums1 is exhausted)
        # while j < n2:
        #     if count == ind1:
        #         ind1el = nums2[j]
        #     if count == ind2:
        #         ind2el = nums2[j]
        #     count += 1
        #     j += 1

        # # If the total number of elements is odd, return the middle element
        # if n3 % 2 == 1:
        #     return float(ind2el)
        # # If the total number of elements is even, return the average of the two middle elements
        # return (ind1el + ind2el) / 2.0