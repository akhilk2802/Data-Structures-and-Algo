class Solution:
    def checkIfPangram(self, sentence: str) -> bool:

        count = Counter(sentence)

        # print(len(count))
        return len(count) == 26
        