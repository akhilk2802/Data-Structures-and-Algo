class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        wordSet = set(wordList)

        if endWord not in wordSet:
            return 0
        
        queue = deque([(beginWord, 1)])

        while queue:

            currentWord, depth = queue.popleft()
            for i in range(len(currentWord)):
                for char in "abcdefghijklmnopqrstuvwxyz":
                    newWord = currentWord[:i] + char + currentWord[i + 1:]
                    # print("newWord : ", newWord)

                    if newWord == endWord:
                        return depth + 1

                    if newWord in wordSet:
                        wordSet.remove(newWord)
                        queue.append((newWord, depth + 1))

        return 0