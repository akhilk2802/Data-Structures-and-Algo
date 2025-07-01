class Solution {

    public void backtrack(List<String> result, int openCount, int closeCount, int n, String current) {

        if (current.length() == 2 * n) {
            result.add(current);
        }

        if (openCount > closeCount) {
            backtrack(result, openCount, closeCount + 1, n, current + ")");
        }
        if (openCount < n) {
            backtrack(result, openCount + 1, closeCount, n, current + "(");
        }
    }

    public List<String> generateParenthesis(int n) {

        List<String> result = new ArrayList<>();
        backtrack(result, 0, 0, n, "");

        return result;
    }
}