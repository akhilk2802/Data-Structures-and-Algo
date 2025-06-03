class Solution:
    def minDeletion(self, s: str, k: int) -> int:

        count = Counter(s)
        if len(count) <= k:
            return 0
        sorted_c = sorted(count.values())
        return sum(sorted_c[:len(sorted_c) - k])
