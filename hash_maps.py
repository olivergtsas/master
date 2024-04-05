class HashMap:
    def __init__(self, size):
        self.size = size
        self.map = [None] * size

    def _hash(self, key):
        return hash(key) % self.size

    def put(self, key, value):
        index = self._hash(key)
        if self.map[index] is None:
            self.map[index] = [(key, value)]
        else:
            for i, (k, _) in enumerate(self.map[index]):
                if k == key:
                    self.map[index][i] = (key, value)
                    break
            else:
                self.map[index].append((key, value))

    def get(self, key):
        index = self._hash(key)
        if self.map[index] is not None:
            for k, v in self.map[index]:
                if k == key:
                    return v
        return None

    def remove(self, key):
        index = self._hash(key)
        if self.map[index] is not None:
            for i, (k, _) in enumerate(self.map[index]):
                if k == key:
                    del self.map[index][i]
                    break

# Let's create a HashMap instance and use it with some sample data
hash_map = HashMap(10)

# Putting some key-value pairs into the hash map
hash_map.put("apple", 5)
hash_map.put("banana", 10)
hash_map.put("orange", 15)

# Getting values for keys
print("Value for 'apple':", hash_map.get("apple"))
print("Value for 'banana':", hash_map.get("banana"))
print("Value for 'orange':", hash_map.get("orange"))
print("Value for 'grape':", hash_map.get("grape"))  # This key doesn't exist, so it will return None

# Removing a key
hash_map.remove("banana")

# Trying to get the value for the removed key
print("Value for 'banana' after removal:", hash_map.get("banana"))  # It should return None now
