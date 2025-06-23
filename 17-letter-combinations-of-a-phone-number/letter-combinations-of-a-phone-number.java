class Solution {
    public List<String> letterCombinations(String digits) {

        Map<Character, String> map = new HashMap<>();
        List<String> result = new ArrayList<>();


        if (digits == null || digits.length() == 0) {
            return result;
        }

        map.put('2', "abc");
        map.put('3', "def");
        map.put('4', "ghi");
        map.put('5', "jkl");
        map.put('6', "mno");
        map.put('7', "pqrs");
        map.put('8', "tuv");
        map.put('9', "wxyz");

        backtrack(digits, 0, "", map, result);
        return result;

    }

    private void backtrack(String digits, int i, String curStr, Map<Character, String> map, List<String> result){
        if (curStr.length() == digits.length()){
            result.add(curStr);
            return;
        }

        String letters = map.get(digits.charAt(i));

        for (char ch: letters.toCharArray()){
            backtrack(digits, i + 1, curStr + ch, map, result);
        }
    }
}