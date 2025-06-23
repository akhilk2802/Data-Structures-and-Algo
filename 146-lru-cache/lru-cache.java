class LRUCache {

    class Node {
        int key;
        int value;

        Node next;
        Node prev;

        public Node (int key, int value) {
            this.key = key;
            this.value = value;
            this.next = null;
            this.prev = null;
        }
    }

    private final int capacity;
    private final Map<Integer, Node> cache;
    private final Node head, tail;

    public LRUCache(int capacity) {

        this.cache = new HashMap<>();
        this.capacity = capacity;
        
        this.head = new Node(-1, -1);
        this.tail = new Node(-1, -1);

        head.next = tail;
        tail.prev = head;
    }
    
    public int get(int key) {

        if (cache.containsKey(key)) {
            Node currentNode = cache.get(key);
            remove(currentNode);
            insertInFront(currentNode);
            return currentNode.value;
        }
        return -1;
    }
    
    public void put(int key, int value) {

        if (cache.containsKey(key)) {
            Node currentNode = cache.get(key);
            remove(currentNode);
            cache.remove(key);
        }

        if (cache.size() >= capacity) {
            Node lastNode = tail.prev;
            remove(lastNode);
            cache.remove(lastNode.key);
        }

        Node newNode = new Node(key, value);
        cache.put(key, newNode);
        insertInFront(newNode);
    }

    public void remove(Node node) {

        node.prev.next = node.next;
        node.next.prev = node.prev;

    }

    public void insertInFront(Node node) {

        node.next = head.next;
        head.next.prev = node;
        node.prev = head;
        head.next = node;

    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */