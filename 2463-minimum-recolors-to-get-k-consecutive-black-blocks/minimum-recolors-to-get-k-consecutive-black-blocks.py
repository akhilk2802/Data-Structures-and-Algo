class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:

        min_whites = blocks[:k].count('W')
        curr_whites = min_whites

        for i in range(k, len(blocks)):
            if blocks[i] == 'W':
                curr_whites += 1
            if blocks[i - k] == 'W':
                curr_whites -= 1
            min_whites = min(min_whites, curr_whites)

        return min_whites