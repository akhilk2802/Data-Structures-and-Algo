class Solution {
    public boolean isAnagram(String s, String t) {

        if (s.length() != t.length()) {
            return false;
        }

        char[] sArray = s.toCharArray();
        char[] tArray = t.toCharArray();

        Arrays.sort(sArray);
        Arrays.sort(tArray);
        
        

        int i = 0, j= 0;
        while (i < sArray.length && j < tArray.length){
            if (sArray[i] != tArray[j]){
                return false;
            }
            i++;
            j++;
        }
        return true;
        
    }
}