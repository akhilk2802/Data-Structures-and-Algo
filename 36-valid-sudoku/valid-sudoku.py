class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rs = defaultdict(set)
        cs = defaultdict(set)
        bs = defaultdict(set)

        for i in range(9):
            for j in range(9):
                num = board[i][j]

                if num == ".":
                    continue
                
                if (num in rs[i] or num in cs[j] or num in bs[(i // 3, j // 3)]):
                    return False
                
                rs[i].add(num)
                cs[j].add(num)
                bs[(i // 3, j // 3)].add(num)

        return True

