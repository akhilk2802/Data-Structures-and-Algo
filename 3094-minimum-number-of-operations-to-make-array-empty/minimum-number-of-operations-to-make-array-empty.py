class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        m = Counter(nums)
        print("map : ", m)
        c = 0

        for _, v in m.items():
            if v == 1:
                return -1
            
            ops = v // 3
            remain = v % 3

            if remain == 0:
                c += ops
            else:
                c += ops + 1

        return c