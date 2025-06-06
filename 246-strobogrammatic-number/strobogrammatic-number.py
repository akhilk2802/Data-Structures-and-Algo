class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        
        s_map = {
            "9":"6",
            "6": "9",
            "8": "8",
            "0": "0",
            "1": "1"
        }

        i, j = 0, len(num) - 1
        
        while i <= j:
            if num[i] not in s_map or s_map[num[i]] != num[j]:
                return False
            i += 1
            j -= 1

        return True