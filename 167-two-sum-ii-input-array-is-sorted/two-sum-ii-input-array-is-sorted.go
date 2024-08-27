func twoSum(numbers []int, target int) []int {
    
    left := 0
    right := len(numbers) - 1

    for left < right {

        total := numbers[left] + numbers[right]

        if total == target{
            return []int{left+1, right+1}
        } else if total < target {
            left ++
        } else {
            right --
        }
    }
    return []int{}
}