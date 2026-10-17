
class HashMap:
    def __init__(self, size=16):
        self.size = size
        self.map = [[] for _ in range(size)]
    
    def _hash(self, key):
        return hash(key) % self.size
    
    def set(self, key, value):
        index = self._hash(key)
        for i, (k, v) in enumerate(self.map[index]):
            if k == key:
                self.map[index][i] = (key, value)
                return
        self.map[index].append((key, value))
    
    def get(self, key):
        index = self._hash(key)
        for k, v in self.map[index]:
            if k == key:
                return v
        return None
    
    def remove(self, key):
        index = self._hash(key)
        for i, (k, v) in enumerate(self.map[index]):
            if k == key:
                self.map[index].pop(i)
                return True
        return False


def main():
    hm = HashMap()
    hm.set("name", "Alice")
    hm.set("age", 25)
    hm.set("city", "NYC")
    print(f"Get name: {hm.get('name')}")
    print(f"Get age: {hm.get('age')}")
    hm.remove("city")
    print(f"Get city after removal: {hm.get('city')}")


if __name__ == "__main__":
    main()
