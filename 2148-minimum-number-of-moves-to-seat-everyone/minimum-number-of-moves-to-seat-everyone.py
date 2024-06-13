class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        if len(seats) != len(students):
            return -1
        sortedSeats = sorted(seats)
        sortedStudents = sorted(students)
        i, j, total = 0, 0, 0
        while i < len(students) and j < len(seats):
            if sortedStudents[i] != sortedSeats[j]:
                total += abs(sortedStudents[i] - sortedSeats[j])
            i += 1
            j += 1
        return total
