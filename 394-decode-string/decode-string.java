class Solution {
    public String decodeString(String s) {
        Stack<String> stack = new Stack<>();

        for (int i = 0; i < s.length(); i++) {
            char ch = s.charAt(i);

            if (ch != ']') {
                stack.push(String.valueOf(ch));
            } else {
                // Step 1: Pop the substring inside brackets
                StringBuilder sub = new StringBuilder();
                while (!stack.peek().equals("[")) {
                    sub.insert(0, stack.pop());
                }

                // Pop the '['
                stack.pop();

                // Step 2: Get the number
                StringBuilder num = new StringBuilder();
                while (!stack.isEmpty() && Character.isDigit(stack.peek().charAt(0))) {
                    num.insert(0, stack.pop());
                }

                int count = Integer.parseInt(num.toString());

                // Step 3: Repeat the substring and push back to stack
                String repeated = sub.toString().repeat(count);
                stack.push(repeated);
            }
        }

        // Final result
        StringBuilder result = new StringBuilder();
        for (String str : stack) {
            result.append(str);
        }

        return result.toString();
    }
}