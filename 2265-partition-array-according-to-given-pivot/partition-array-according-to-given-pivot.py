class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        
        l = []
        r = []

        for i in range(len(nums)):
            if nums[i] < pivot:
                l.append(nums[i])
            elif nums[i] > pivot:
                r.append(nums[i])

        # print("left and right : ", l, r)

        result = []
        for num in l:
            result.append(num)

        for i in range(len(nums) - (len(l) + len(r))):
            result.append(pivot)

        for num in r:
            result.append(num)

        # print("Number is -> ", result)
        return result


        # l, r = 0, 1
        

        # while r < len(nums):
            
        #     # if left pointers value is greater than right pointers value, swap them untill i reach the pivot
        #     if nums[l] > nums[r]:
        #         nums[l], nums[r] = nums[r], nums[l]
                
        #         l += 1
        #         r += 1
        #     # once i reach the pivot element, i want to stop moving the left pointer and keep it on the pivot element and move only the right pointer, where ever i find the element less than or equal to pivot element, i will add it to the left pointer position and increase the left pointer to next (+1), once i hit the right pointer to the end of the list i will return the array 
        #     if nums[l] == pivot:





                
