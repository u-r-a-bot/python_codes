from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.memory = []
        self.capacity = capacity
        self.cache_hits = 0
        self.cache_misses = 0

    def access_page(self, page):
        if page in self.cache:

            self.cache.move_to_end(page)
            self.cache_hits += 1
        else:
            if len(self.cache) >= self.capacity:

                removed_page, _ = self.cache.popitem(last=False)
                self.memory.remove(removed_page)

            self.cache[page] = None
            self.memory.insert(0, page)
            self.cache_misses += 1

    def display_cache_memory(self):
        print("Cache Content:", list(self.cache.keys()))
        print(f"Cache Hits: {self.cache_hits}, Cache Misses: {self.cache_misses}")
        print("----------------------")

# Example usage:
capacity = 3
lru_cache = LRUCache(capacity)

while True:
    lru_cache.access_page(int(input("Enter a number  ")))
    lru_cache.display_cache_memory()
