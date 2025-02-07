class Solution:
    def frequencySort(self, s: str) -> str:

        freq = Counter(s)
        result = ''.join(char * times for char, times in freq.most_common())
        
        return result