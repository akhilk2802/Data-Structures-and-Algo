class Solution:
    def canPermutePalindrome(self, s: str) -> bool:

        
        '''
        c = 3

        '''
        
        count = Counter(s)
        # print("count : ", count)
        even = 0
        odd = 0

        for k, v in count.items():
            if v % 2 == 0:
                even += 1
            else:
                odd += 1

        return odd < 2


