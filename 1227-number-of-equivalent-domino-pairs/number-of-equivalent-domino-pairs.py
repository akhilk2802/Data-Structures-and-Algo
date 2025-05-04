class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:

        sort_dominoes = [tuple(sorted(pair)) for pair in dominoes]

        sort_dominoes.sort()

        hash_map = {}

        for pair in sort_dominoes:
            if pair in hash_map:
                hash_map[pair] += 1
            else:
                hash_map[pair] = 1

        print("hash_map -> ", hash_map)
        result = 0
        for c in hash_map.values():
            result += c * (c - 1) // 2

        return result