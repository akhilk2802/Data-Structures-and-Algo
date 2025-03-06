class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        
        substring_count = {}
        
        for word in arr:
            n = len(word)
            seen = set()
            for i in range(n):
                for j in range(i + 1, n + 1):
                    substr = word[i:j]
                    if substr not in seen:
                        seen.add(substr)
                        substring_count[substr] = substring_count.get(substr, 0) + 1

        result = []
        for word in arr:
            min_length = float("inf")
            shortest_substr = ""

            for i in range(len(word)):
                for j in range(i + 1, len(word) + 1):
                    substr = word[i:j]
                    if substring_count[substr] == 1:
                        if len(substr) < min_length:
                            min_length = len(substr)
                            shortest_substr = substr
                        elif len(substr) == min_length and substr < shortest_substr:
                            shortest_substr = substr

            result.append(shortest_substr if shortest_substr else "")

        return result