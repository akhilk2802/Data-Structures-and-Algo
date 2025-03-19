class Solution:
    def beautySum(self, s: str) -> int:

        '''
        for this problem the brute force Solution will be something like -> 
        find all the possible substring and keep adding the beauty to it 

        so i am going to use a helper function to calculate the beauty for each of the substring
        '''
        beauty = 0

        def find_beauty(substring):

            count = Counter(substring)
            sorted_count = dict(sorted(count.items(), key=lambda x: x[1], reverse=True))
            # print("counter : ", count)
            if len(sorted_count) > 1:
                first_val = list(sorted_count.values())[0]
                last_val = list(sorted_count.values())[-1]
                val = (last_val - first_val)
                return val
            elif len(sorted_count) <= 1:
                return 0


        n = len(s)
        for i in range(n):
            for j in range(i, n):
                # print("i and j : ", s[i:j+1])
                beauty += find_beauty(s[i:j+1])
            
        return -beauty
        