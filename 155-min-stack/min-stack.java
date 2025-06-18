import javax.xml.crypto.dsig.keyinfo.RetrievalMethod;

class MinStack {

    List<Integer> minStack;
    List<Integer> stack;
    
    public MinStack() {

        minStack = new ArrayList<>();
        stack = new ArrayList<>();

    }
    
    public void push(int val) {

        stack.add(val);
        if (minStack.size() == 0 || minStack.get(minStack.size() - 1) >= val) {
            minStack.add(val);
        }
    }
    
    public void pop() {

        int popVal = stack.remove(stack.size() - 1);
        if (minStack.size() > 0 && minStack.get(minStack.size() - 1).equals(popVal)) {
            minStack.remove(minStack.size() - 1);
        }
    }
    
    public int top() {
        return stack.get(stack.size() - 1);
        
    }
    
    public int getMin() {
        return minStack.get(minStack.size() - 1);
        
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