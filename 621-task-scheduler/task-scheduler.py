class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        count = list(Counter(tasks).values())
        max_freq = max(count)

        max_freq_count = count.count(max_freq)

        min_Intervals = (max_freq - 1) * (n+1) + max_freq_count

        return max(min_Intervals, len(tasks))
        



        