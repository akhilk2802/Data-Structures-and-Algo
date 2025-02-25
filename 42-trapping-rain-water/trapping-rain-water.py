class Solution:
    def trap(self, height: List[int]) -> int:
        
        # algo - 
        # 1. Start with two pointer
        # 2. left starts from 0 and right from the last element 
        # 3. maintain the max height from each side 
        # 4. Keep shifting the pointers towards each other comparing with the height 
        # 5. if i find any height higher than previous, i would replace existing and find the total water it can hold

        l, r = 0, len(height) - 1
        maxLeft = height[l]
        maxRight = height[r]

        totalWater = 0

        while l < r:
            if height[l] <= height[r]:
                if height[l] < maxLeft:
                    totalWater += maxLeft - height[l]
                if height[l] > maxLeft:
                    maxLeft = height[l]
                l += 1
            else: 
                if height[r] < maxRight:
                    totalWater += maxRight - height[r]
                if height[r] > maxRight:
                    maxRight = height[r]
                r -= 1

        return totalWater

                




        return totalWater