from collections import OrderedDict

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.min_freq = 0
        self.cache = {}  # Key -> (value, frequency)
        self.freq_map = defaultdict(OrderedDict)  # Frequency -> {key: value}

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        # Get the value and current frequency
        value, freq = self.cache[key]
        
        # Remove the key from the current frequency list
        del self.freq_map[freq][key]
        if not self.freq_map[freq]:  # If no more keys at this freq
            del self.freq_map[freq]
            if self.min_freq == freq:
                self.min_freq += 1
        
        # Update frequency and move to new frequency
        self.cache[key] = (value, freq + 1)
        self.freq_map[freq + 1][key] = value
        
        return value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        
        if key in self.cache:
            # Update value and use get() to adjust frequency
            self.cache[key] = (value, self.cache[key][1])
            self.get(key)  # Update frequency
            return
        
        # If the cache is full, remove the least frequently used key
        if len(self.cache) >= self.capacity:
            lfu_key, _ = self.freq_map[self.min_freq].popitem(last=False)
            del self.cache[lfu_key]
            if not self.freq_map[self.min_freq]:  # Remove freq entry if empty
                del self.freq_map[self.min_freq]

        # Insert new key with frequency 1
        self.cache[key] = (value, 1)
        self.freq_map[1][key] = value
        self.min_freq = 1  # Reset min frequency to 1


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)