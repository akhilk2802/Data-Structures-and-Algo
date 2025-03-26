class Solution:
    def trap(self, height: List[int]) -> int:
        
        # algo - 
        # 1. Start with two pointer
        # 2. left starts from 0 and right from the last element 
        # 3. maintain the max height from each side 
        # 4. Keep shifting the pointers towards each other comparing with the height 
        # 5. if i find any height higher than previous, i would replace existing and find the total water it can hold

        l, r = 0, len(height) - 1
        max_left = height[l]
        max_right = height[r]
        total = 0

        while l < r:
            if height[l] <= height[r]:
                if height[l] > max_left:
                    max_left = height[l]
                else:
                    total += (max_left - height[l])
                l += 1
            else:
                if height[r] > max_right:
                    max_right = height[r]
                else:
                    total += (max_right - height[r])
                r -= 1

        return total