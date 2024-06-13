class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        if len(seats) != len(students):
            return -1
        sortedSeats = sorted(seats)
        sortedStudents = sorted(students)
        total = 0
        for seat, student in zip(sortedSeats, sortedStudents):
            total += abs(seat - student)
        return total
