func maxArea(height []int) int {

    left := 0
    right := len(height) - 1
    max := 0

    for left < right {

        h := mini(height[left], height[right])
        w := right - left

        area := h * w
        max = maxi(max, area)

        if height[left] < height[right] {
            left++
        } else {
            right--
        }
        
    }
    return max
    
}

func mini(a, b int) int{
    if a < b {
        return a
    } else {
        return b
    }
}

func maxi(a, b int) int{
    if a > b {
        return a
    } else {
        return b
    }
}