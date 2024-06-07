class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        roots = set(dictionary)
        print(roots)
        words = sentence.split()
        print(words)
        result = []

        for word in words:
            for i in range(len(words) + 1):
                prefix = word[:i]
                if prefix in roots:
                    result.append(prefix)
                    break
            else:
                result.append(word)

        return ' '.join(result)