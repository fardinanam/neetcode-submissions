class MyHashSet:

    def __init__(self):
        self.capacity = 7
        self.loadFactor = 0.75
        self.size = 0

        self.buckets = [None] * self.capacity

    def add(self, key: int) -> None:
        if self.contains(key):
            return

        if self.size / self.capacity >= self.loadFactor:
            self.__resize()

        hashedKey = self.__getHashKey(key)

        if not self.buckets[hashedKey]:
            self.buckets[hashedKey] = []
        
        self.buckets[hashedKey].append(key)


    def remove(self, key: int) -> None:
        if not self.contains(key):
            return
        
        hashedKey = self.__getHashKey(key)
        self.buckets[hashedKey].remove(key)
        

    def contains(self, key: int) -> bool:
        hashedKey = self.__getHashKey(key)

        if not self.buckets[hashedKey]:
            return False
        
        for k in self.buckets[hashedKey]:
            if k == key:
                return True
        
        return False
    
    def __getHashKey(self, value):
        return abs(hash(value)) % self.capacity
    
    def __resize(self):
        oldBuckets = self.buckets
        self.capacity *= 2
        self.buckets = [None] * self.capacity
        self.size = 0

        for bucket in oldBuckets:
            for key in bucket:
                self.add(key)

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)