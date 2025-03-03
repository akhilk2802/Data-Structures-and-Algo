class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        
        l = []
        r = []

        for i in range(len(nums)):
            if nums[i] < pivot:
                l.append(nums[i])
            elif nums[i] > pivot:
                r.append(nums[i])

        print("left and right : ", l, r)

        result = []
        for num in l:
            result.append(num)
        
        for i in range(len(nums) - (len(l) + len(r))):
            result.append(pivot)

        for num in r:
            result.append(num)

        print("Number is -> ", result)
        return result