class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:

        lenS1 = len(s1)
        lenS2 = len(s2)
        if lenS1 != lenS2:
            return False

        counter1 = Counter(s1)
        counter2 = Counter(s2)

        if counter1 != counter2:
            return False

        count = 0
        for i in range(lenS1):
            if s1[i] != s2[i]:
                count += 1

        print("Count : ", count)

        if count > 2:
            return False
    
        return True