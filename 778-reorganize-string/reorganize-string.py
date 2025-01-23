from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        print("Count:", count)

        max_freq = max(count.values())
        if max_freq > (len(s) + 1) // 2:
            return ""

        sorted_chars = sorted(count.items(), key=lambda x: -x[1])
        print("Sorted characters:", sorted_chars)

        result = [None] * len(s)
        index = 0

        for char, freq in sorted_chars:
            for _ in range(freq):
                result[index] = char
                index += 2
                if index >= len(s):
                    index = 1
        return "".join(result)