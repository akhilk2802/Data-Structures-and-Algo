class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        counter = list(Counter(tasks).values())
        print("Count : ", counter)
        max_freq = max(counter)

        max_freq_count = counter.count(max_freq)
        print("max freq count : ", max_freq_count)

        min_Intervals = (max_freq - 1) * (n+1) + max_freq_count

        return max(min_Intervals, len(tasks))
        



        