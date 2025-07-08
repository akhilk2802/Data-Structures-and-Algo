class Logger {

    Map<String, Integer> freq;

    public Logger() {

        this.freq = new HashMap<>();
        
    }
    
    public boolean shouldPrintMessage(int timestamp, String message) {

        if (!this.freq.containsKey(message)) {
            this.freq.put(message, timestamp);
            return true;
        }

        Integer oldTimestamp = this.freq.get(message);
        if (timestamp - oldTimestamp >= 10) {
            this.freq.put(message, timestamp);
            return true;
        } else return false;
        
    }
}

/**
 * Your Logger object will be instantiated and called as such:
 * Logger obj = new Logger();
 * boolean param_1 = obj.shouldPrintMessage(timestamp,message);
 */