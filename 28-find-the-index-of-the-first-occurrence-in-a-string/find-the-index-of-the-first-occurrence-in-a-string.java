class Solution {
    public int strStr(String haystack, String needle) {

        int l1 = haystack.length();
        int l2 = needle.length();

        for (int i = 0; i < l1 - l2 + 1; i++){
            String match = haystack.substring(i, i + l2);
            if (match.equals(needle)) {
                return i;
            }
        }
        return -1;
    }
}