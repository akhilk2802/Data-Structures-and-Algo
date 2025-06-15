class Solution {
    public boolean isValidSudoku(char[][] board) {

        Map<Integer, Set<Character>> rs = new HashMap<>();
        Map<Integer, Set<Character>> cs = new HashMap<>();
        Map<Integer, Set<Character>> bs = new HashMap<>();

        for (int i = 0; i < 9; i++) {
            rs.put(i, new HashSet<>());
            cs.put(i, new HashSet<>());
            bs.put(i, new HashSet<>());
        }

        for (int i = 0; i < 9; i++){
            for (int j = 0; j < 9; j++){

                char val = board[i][j];
                if (val == '.'){
                    continue;
                }

                int boxIndex = (i / 3) * 3 + (j / 3);
                
                if (rs.get(i).contains(val) || cs.get(j).contains(val) || bs.get(boxIndex).contains(val)){
                    return false;
                }
                
                rs.get(i).add(val);
                cs.get(j).add(val);
                bs.get(boxIndex).add(val);
            }
        }
        return true;
    }
}