class Solution:
    def getHappyString(self, n: int, k: int) -> str:

        # algo -
        # 1. Generate all the happy string of size n 
        # 2. Return the kth string

        # algo improve - 
        # 1. Generate the happy string untill i reach kth element 
        # 2. Once reached return the string
        # 3. No need to store the strings as well 
        chars = {"a", "b", "c"}
        happy = []

        def generate_strings(chars, n, current=""):
            if len(current) == n:
                happy.append(current[:])
                return 

            for ch in chars:
                if not current or current[-1] != ch:
                    generate_strings(chars, n, current + ch)

        generate_strings(chars, n)
        happy.sort()

        if len(happy) >= k:
            return happy[k-1]

        return ""
