class Solution {
    public List<String> letterCombinations(String digits) {

        Map<Integer, String> map = new HashMap<>();

        map.put(2, "abc");
        map.put(3, "def");
        map.put(4, "ghi");
        map.put(5, "jkl");
        map.put(6, "mno");
        map.put(7, "pqrs");
        map.put(8, "tuv");
        map.put(9, "wxyz");        

        List<String> result = new ArrayList<>();
        if (digits == null || digits.length() == 0) return result;

        backtrack(result, "", map, digits, 0);

        return result;
    }

    public void backtrack(List<String> result, String current, Map<Integer, String> map, String digits, int index) {
        if (current.length() == digits.length()) {
            result.add(current);
            return;
        }

        char digit = digits.charAt(index);
        String letters = map.get(digit - '0');

        for (char c : letters.toCharArray()) {
            backtrack(result, current + c, map, digits, index + 1);
        }
        
    }

}