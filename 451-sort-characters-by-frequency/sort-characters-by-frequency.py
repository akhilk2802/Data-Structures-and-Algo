class Solution:
    def frequencySort(self, s: str) -> str:

        freq = Counter(s)
        return ''.join(char * times for char, times in freq.most_common())