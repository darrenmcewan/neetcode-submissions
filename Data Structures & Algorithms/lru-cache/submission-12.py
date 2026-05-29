class LRUCache:

    def __init__(self, capacity: int):
        self.LRUCache = {}
        self.capacity = capacity
        self.lru = []

    def get(self, key: int) -> int:
        if key not in self.LRUCache:
            return -1

        self.lru.remove(key)
        self.lru.append(key)

        return self.LRUCache[key]

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.LRUCache:
            self.LRUCache[key] = value
            self.lru.remove(key)
            self.lru.append(key)
            return

        if len(self.LRUCache) == self.capacity:
            least_recent = self.lru.pop(0)
            self.LRUCache.pop(least_recent)

        self.LRUCache[key] = value
        self.lru.append(key)