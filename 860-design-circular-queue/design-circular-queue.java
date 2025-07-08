class ListNode{

    int val;
    ListNode next;

    public ListNode(int val) {
        
        this.val = val;
        this.next = null;

    }
}

class MyCircularQueue {
    
    int count;
    int capacity;
    ListNode head;
    ListNode tail;

    public MyCircularQueue(int k) {
        this.capacity = k;
        this.count = 0;
        this.head = null;
        this.tail = null;
        
    }
    
    public boolean enQueue(int value) {

        if (this.count >= this.capacity) {
            return false;
        }

        ListNode newNode = new ListNode(value);

        if (count == 0) {
            head = newNode;
            tail = newNode;
        } else {
            tail.next = newNode;
            tail = newNode;
        }

        count++;
        return true;
        
    }
    
    public boolean deQueue() {
        if (count == 0) {
            return false;
        }

        head = head.next;
        count--;

        if (count == 0) {
            tail = null;
        }

        return true;
        
    }
    
    public int Front() {
        if (count == 0) {
            return -1;
        }
        return head.val;
    }

    public int Rear() {
        if (count == 0) {
            return -1;
        }
        return tail.val;
    }

    public boolean isEmpty() {
        return count == 0;
    }

    public boolean isFull() {
        return count == capacity;
    }
}

/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * MyCircularQueue obj = new MyCircularQueue(k);
 * boolean param_1 = obj.enQueue(value);
 * boolean param_2 = obj.deQueue();
 * int param_3 = obj.Front();
 * int param_4 = obj.Rear();
 * boolean param_5 = obj.isEmpty();
 * boolean param_6 = obj.isFull();
 */