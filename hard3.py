class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = []

    def put(self, key):
        if key in self.cache:
            pass         
        else:
            if len(self.cache) == self.capacity:
                self.cache.pop()  
            self.cache.append(key)

    def get(self):
        return self.cache

cache = LRUCache(3)

cache.put(1)
cache.put(2)
cache.put(3)
cache.put(4)

print(cache.get())
