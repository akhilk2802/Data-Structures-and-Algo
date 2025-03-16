class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:

        '''
        Start with brute force approach - 

        first i know there are n cars, and ranks 
        now i can 
        '''
        l = 1
        r = min(ranks) * (cars * cars)

        def car_repair(time):
            total_car_repair = 0

            for rank in ranks:
                car_repaired = int((time / rank) ** 0.5)
                total_car_repair += car_repaired
                if total_car_repair >= cars:
                    return True
            return False

        while l < r:
            mid = (l + r) // 2

            if car_repair(mid):
                r = mid
            else:
                l = mid + 1
        
        return l