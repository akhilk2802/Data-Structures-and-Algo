class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        m = defaultdict(int)

        for i in range(len(s) - 1, -1, -1):
            if s[i] not in m:
                m[s[i]] = i
        
        result = []
        size = 0
        end = 0

        for i in range(len(s)):
            char = s[i]

            if m[char] > end:
                end = m[char]

            size += 1
            if i == end:
                result.append(size)
                size = 0

        # print("result -> ", result)
        return result



        