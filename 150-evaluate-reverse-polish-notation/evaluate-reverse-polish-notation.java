class Solution {
    public int evalRPN(String[] tokens) {

        Stack<String> stack = new Stack<>();
        Set<String> ops = new HashSet<>();

        ops.add("+");
        ops.add("-");
        ops.add("/");
        ops.add("*");

        for (String c: tokens) {

            if (!ops.contains(c)) {
                stack.add(c);
            } else if (stack.size() >= 2) {
                int value1 = Integer.parseInt(stack.pop());
                int value2 = Integer.parseInt(stack.pop());
                if (c.equals("+")) {    
                    int value3 = value1 + value2;
                    stack.add(Integer.toString(value3));
                }
                if (c.equals("-")) {
                    int value3 = value2 - value1;
                    stack.add(Integer.toString(value3));
                }
                if (c.equals("*")) {
                    int value3 = value2 * value1;
                    stack.add(Integer.toString(value3));
                }
                if (c.equals("/")) {
                    int value3 = value2 / value1;
                    stack.add(Integer.toString(value3));
                }
            }
        }

        return Integer.parseInt(stack.pop());
    }
}