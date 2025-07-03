class Solution {
    public char kthCharacter(int k) {

        // String pattern = "a";

        // while (pattern.length() <= k) {
        //     String newP = "";
        //     for (int i = 0; i < pattern.length(); i++) {
        //         char ch = pattern.charAt(i);
        //         char nextChar = (char) ((ch - 'a' + 1) % 26 + 'a');
        //         newP += nextChar;
        //     }
        //     pattern += newP;
        // }
        // return pattern.charAt(k - 1);

        StringBuilder pattern = new StringBuilder("a");

        while (pattern.length() < k) {
            int len = pattern.length();
            for (int i = 0; i < len && pattern.length() < k; i++){
                char ch = pattern.charAt(i);
                char nextChar = (char) ((ch - 'a' + 1) % 26 + 'a');
                pattern.append(nextChar);
            }
        }

        return pattern.charAt(k - 1);
    }
}