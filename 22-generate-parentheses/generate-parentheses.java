class Solution {
    public List<String> generateParenthesis(int n) {

        List<String> result = new ArrayList<>();

        backtrack("", 0, 0, n, result);
        return result;
    }

    public void backtrack(String current, int openP, int closeP, int n, List<String> result) {

        if (current.length() == 2 * n) {
            result.add(current);
        }

        if (openP > closeP){
            backtrack(current + ")", openP, closeP + 1, n, result);
        }
        if (openP < n){
            backtrack(current + "(", openP + 1, closeP, n, result);
        }
    }
}