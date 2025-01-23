from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:

        result = ""

        count = Counter(s)
        print("Count : ", count)

        if any(freq > (len(s) + 1) // 2 for freq in count.values()):
            return ""

        max_heap = [(-freq, char) for char, freq in count.items()]
        heapq.heapify(max_heap)

        print("Max Heap :", max_heap)

        result = []
        prev_char = None
        prev_freq = 0

        while max_heap:
            freq, char = heapq.heappop(max_heap)
            result.append(char)
            if prev_freq < 0:
                heapq.heappush(max_heap, (prev_freq, prev_char))
            prev_char = char
            prev_freq = freq + 1

        return "".join(result)