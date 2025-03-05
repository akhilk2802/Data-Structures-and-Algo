class Solution:
    def alienOrder(self, words: List[str]) -> str:

        adj_list = defaultdict(list)
        for word in words:
            for char in word:
                if char not in adj_list:
                    adj_list[char] = []

        def diff_character(word1, word2):
            n1 = len(word1)
            n2 = len(word2)
            i, j = 0, 0
            while i < n1 and j < n2:
                if word1[i] == word2[j]:
                    i += 1
                    j += 1
                else: 
                    return [word1[i], word2[j]]
            return None

        n = len(words)
        indegree = defaultdict(int)
        for i in range(1, n):
            current_word = words[i]
            prev_word = words[i-1]

            if len(prev_word) > len(current_word) and prev_word.startswith(current_word):
                return ""
            edge = diff_character(current_word, prev_word)

            if edge:
                node1, node2 = edge

                if node2 not in adj_list[node1]:
                    adj_list[node1].append(node2)
                    indegree[node2] += 1

        queue = deque()
        topo = []

        for char in adj_list:
            if indegree[char] == 0:
                queue.append(char)

        while queue:
            node = queue.popleft()
            topo.append(node)

            for neighbor in adj_list[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
                    
        if len(topo) != len(adj_list):
            return ""

        return "".join(topo[::-1])