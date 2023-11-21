from collections import deque

class FIFOCache:
    def __init__(self, capacity):
        self.cache = deque(maxlen=capacity)
        self.cache_hits = 0
        self.cache_misses = 0

    def access_page(self, page):
        if page in self.cache:
            self.cache_hits += 1
        else:
            self.cache_misses += 1
            if len(self.cache) == self.cache.maxlen:
                self.cache.popleft()
            self.cache.append(page)

    def display_cache(self):
        print("FIFO Cache State:", list(self.cache))
        print(f"Cache Hits: {self.cache_hits}, Cache Misses: {self.cache_misses}")
        print("\n")


fifo_cache = FIFOCache(3)

while True:
    fifo_cache.access_page(int(input("Enter a number  ")))
    fifo_cache.display_cache()