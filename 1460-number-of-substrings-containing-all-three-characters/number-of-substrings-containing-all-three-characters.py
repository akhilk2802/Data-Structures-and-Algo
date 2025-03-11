class Solution:
    def numberOfSubstrings(self, s: str) -> int:

        '''
        brute force solution - 
        1. Have two for loops, account for each of the substrings 
        2. check if each substring contains abc, if it does, increase the count 
        3. Time complexity - O(n^2)

        optimised solution - 
        1. Sliding Window Approach 
        2. 
        '''

        l = 0
        n = len(s)
        result = 0
        count = defaultdict(int)

        for r in range(n):
            count[s[r]] += 1

            while len(count) == 3:
                result += n - r
                count[s[l]] -= 1

                if count[s[l]] == 0:
                    count.pop(s[l])

                l += 1

        return result
            
