class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        
        # Minimum number of repetitions to cover at least the length of B
        min_repeats = -(-len(B) // len(A))  # Equivalent to math.ceil(len(B) / len(A))
        
        # Create repeated versions of A to check
        repeated_once = A * min_repeats
        repeated_twice = A * (min_repeats + 1)

        # Check if B is a substring of repeated_once or repeated_twice
        if B in repeated_once:
            return min_repeats
        elif B in repeated_twice:
            return min_repeats + 1
        
        # If B is not a substring, return -1
        return -1
        