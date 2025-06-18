

import javax.xml.crypto.dsig.keyinfo.RetrievalMethod;

class MinStack {

    Stack<Integer> minStack;
    Stack<Integer> stack;
    
    public MinStack() {

        minStack = new Stack<>();
        stack = new Stack<>();

    }
    
    public void push(int val) {

        stack.add(val);
        if (minStack.size() == 0 || minStack.peek() >= val) {
            minStack.add(val);
        }
    }
    
    public void pop() {

        int popVal = stack.pop();
        if (minStack.size() > 0 && minStack.peek().equals(popVal)) {
            minStack.pop();
        }
    }
    
    public int top() {

        return stack.peek();
        
    }
    
    public int getMin() {

        return minStack.peek();
        // return stack.peek();
        
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(val);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */