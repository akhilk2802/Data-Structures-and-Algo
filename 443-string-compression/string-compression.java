class Solution {
    public int compress(char[] chars) {
        
        int index = 0;
        int i = 0;

        while ( i < chars.length ){
            char current_char = chars[i];
            int count = 0;

            while ((i < chars.length) && (chars[i] == current_char)){
                i++;
                count++;
            }
            chars[index] = current_char;
            index++;

            if (count > 1){
                for (char c : String.valueOf(count).toCharArray()){
                    chars[index] = c;
                    index++;
                }
            }
        }
        return index;
    }
}