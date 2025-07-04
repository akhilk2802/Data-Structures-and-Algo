class Solution {

    public int countPalindrome(String s, int start, int end) {

        int c = 0;
        while (start >= 0 && end < s.length() && s.charAt(start) == s.charAt(end)) {
            c += 1;
            start -= 1;
            end += 1;
        }
        return c;
    }

    public int countSubstrings(String s) {

        int count = 0;
        for (int i = 0; i < s.length(); i++) {
            
            count += countPalindrome(s, i, i);
            count += countPalindrome(s, i, i + 1);
        }
        return count;
    }
}