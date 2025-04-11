class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        
        count = 0

        for x in range(low, high+1):
            str_x = str(x)
            len_x = len(str_x)
            mid = len_x // 2

            if len_x % 2 == 0:
                mid = len_x // 2
                left_half = str_x[:mid]
                right_half = str_x[mid:]

                if sum(int(ch) for ch in left_half) == sum(int(ch) for ch in right_half):
                    count += 1
        # print("count -> ", count)
        return count

            





        