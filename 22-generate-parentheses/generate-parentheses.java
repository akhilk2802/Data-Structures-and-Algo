class Solution {
    
    List<String> result = new ArrayList<>();

    public List<String> generateParenthesis(int n) {    
        
        backtrack("", 0, 0, n);
        return result;
    }
    
    private void backtrack(String current, int openCount, int closeCount, int total) {

        if (current.length() == 2 * total) {
            result.add(current);
        }

        if (openCount > closeCount) {
            backtrack(current + ")", openCount, closeCount + 1, total);
        } 
        if (openCount < total) {
            backtrack(current + "(", openCount + 1, closeCount, total);
        }
    }
}