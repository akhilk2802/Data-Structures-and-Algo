class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:

        # Algo - 
        # 1. Create a heap 
        # 2. remove the first two elements - x and y
        # 3. find the min between x and y 
        # 4. do the operation
        # 5. add the element again to heap
        # 6. run a for loop to compare with k, also keep a count of number of operations
        # 7. if all the elements are greater than k, return the count, else perform the function again 

        heapq.heapify(nums)
        c = 0

        while nums:
            
            if nums[0] >= k:
                return c

            x = heapq.heappop(nums)
            y = heapq.heappop(nums)

            print("x and y : ", x, y)
            val = min(x, y) * 2 + max(x, y)
            heapq.heappush(nums, val)
            c += 1

            print("val here is : ", val)
        
        return -1