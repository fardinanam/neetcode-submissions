class MyHashMap:

    def __init__(self):
        self.capacity = 7
        self.size = 0
        self.loadFactor = 0.75
        self.buckets = [None] * self.capacity

    def put(self, key: int, value: int) -> None:
        pair = self.__getPair(key)

        if pair is not None:
            pair[1] = value
            return
        
        hashedKey = self.__hash(key)
        
        if self.buckets[hashedKey] is None:
            self.buckets[hashedKey] = []
        
        self.buckets[hashedKey].append([key, value])
        self.size += 1
        
        if self.size / self.capacity >= self.loadFactor:
            self.__resize()

    def get(self, key: int) -> int:
        pair = self.__getPair(key)

        if pair is None:
            return -1
        
        return pair[1]

    def remove(self, key: int) -> None:
        pair = self.__getPair(key)

        if pair is None:
            return
        
        hashedKey = self.__hash(key)
        self.buckets[hashedKey].remove(pair)
        self.size -= 1

    def __getPair(self, key) -> bool:
        hashedKey = self.__hash(key)

        if self.buckets[hashedKey] is None:
            return None
        
        for pair in self.buckets[hashedKey]:
            if key == pair[0]:
                return pair
        
        return None
    
    def __hash(self, key) -> int:
        return abs(hash(key)) % self.capacity

    def __resize(self) -> None:
        if self.size / self.capacity < self.loadFactor:
            return
        
        oldBuckets = self.buckets
        self.capacity *= 2
        self.size = 0
        self.buckets = [None] * self.capacity

        for bucket in oldBuckets:
            if bucket is not None:
                for k, v in bucket:
                    self.put(k, v)
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)