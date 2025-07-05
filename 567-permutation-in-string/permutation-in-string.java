class Solution {
    public boolean checkInclusion(String s1, String s2) {

        char[] charsS1 = s1.toCharArray();
        Arrays.sort(charsS1);
        String sortedS1 = new String(charsS1);

        int n = sortedS1.length(), m = s2.length();

        for (int i = 0; i < m - n + 1; i++) {
            
            String partS2 = s2.substring(i, i + n);
            char[] charsPartS2 = partS2.toCharArray();
            Arrays.sort(charsPartS2);
            String sortedPartS2 = new String(charsPartS2);

            if(sortedS1.equals(sortedPartS2)){
                return true;
            }

        }
        return false;
    }
}