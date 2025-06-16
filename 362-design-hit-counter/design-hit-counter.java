class HitCounter {

    private Map<Integer, Integer> count;

    public HitCounter() {
        this.count = new HashMap<>();
    }
    
    public void hit(int timestamp) {
        count.put(timestamp, count.getOrDefault(timestamp, 0) + 1);
    }
    
    public int getHits(int timestamp) {
        int totalCount = 0;
        for (int time : count.keySet()) {
            if (time > timestamp - 300 && time <= timestamp) {
                totalCount += count.get(time);
            }
        }
        return totalCount;
    }
}

/**
 * Your HitCounter object will be instantiated and called as such:
 * HitCounter obj = new HitCounter();
 * obj.hit(timestamp);
 * int param_2 = obj.getHits(timestamp);
 */