class MyHashMap {

    private static class Node {
        int key, value;
        Node next;
        Node(int key, int value) {
            this.key = key;
            this.value = value;
        }
    }

    private final int SIZE = 1009;  // Prime number to reduce collisions
    private Node[] buckets;

    public MyHashMap() {
        buckets = new Node[SIZE];
    }

    private int hash(int key) {
        return key % SIZE;
    }

    public void put(int key, int value) {
        int i = hash(key);
        if (buckets[i] == null) {
            buckets[i] = new Node(key, value);
        } else {
            Node curr = buckets[i];
            while (curr != null) {
                if (curr.key == key) {
                    curr.value = value;  // Overwrite
                    return;
                }
                if (curr.next == null) break;
                curr = curr.next;
            }
            curr.next = new Node(key, value);  // Append new
        }
    }

    public int get(int key) {
        int i = hash(key);
        Node curr = buckets[i];
        while (curr != null) {
            if (curr.key == key) return curr.value;
            curr = curr.next;
        }
        return -1;
    }

    public void remove(int key) {
        int i = hash(key);
        Node curr = buckets[i], prev = null;
        while (curr != null) {
            if (curr.key == key) {
                if (prev == null) {
                    buckets[i] = curr.next;
                } else {
                    prev.next = curr.next;
                }
                return;
            }
            prev = curr;
            curr = curr.next;
        }
    }
}