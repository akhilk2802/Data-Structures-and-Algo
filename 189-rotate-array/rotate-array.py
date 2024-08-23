class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n == 1 or k == 0 or k % n == 0:
            return
        k = k % n
        temp = nums[-k:]      
        temp.extend(nums[:n-k])
        nums[:] = temp
