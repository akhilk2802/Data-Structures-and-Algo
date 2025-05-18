class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        len_flowerbed = len(flowerbed)

        count = 0
        for i in range(len_flowerbed):

            if flowerbed[i] == 0:

                empty_left_plot = (i == 0) or (flowerbed[i - 1] == 0)
                empty_right_plot = (i == len_flowerbed - 1) or (flowerbed[i + 1] == 0)

                if empty_left_plot and empty_right_plot:
                    flowerbed[i] = 1
                    count += 1

        return count >= n