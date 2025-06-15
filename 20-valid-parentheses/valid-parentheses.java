class Solution {
    public boolean isValid(String s) {

        Map<String, String> map = new HashMap<>();

        map.put("(", ")");
        map.put("{", "}");
        map.put("[", "]");

        List<String> stack = new ArrayList<>();

        for (int i = 0; i < s.length(); i++ ){

            char c = s.charAt(i);
            String str = String.valueOf(c);

            if (map.containsKey(str)) {
                stack.add(str);
            } else {
                if (stack.isEmpty()) {
                    return false;
                }

                String lastOpen = stack.remove(stack.size() - 1);
                if (!map.get(lastOpen).equals(str)){
                    return false;
                }
            }
        }
        return stack.isEmpty();
    }
}