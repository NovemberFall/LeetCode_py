class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashMap:
    DEFAULT_CAPACITY = 16
    DEFAULT_LOAD_FACTOR = 0.75
    SCALE_FACTOR = 2

    def __init__(self, capacity=DEFAULT_CAPACITY, load_factor=DEFAULT_LOAD_FACTOR):
        if capacity <= 0:
            raise ValueError("Capacity must be positive")
        self.array = [None] * capacity
        self.size = 0
        self.load_factor = load_factor

    def __len__(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def clear(self):
        self.array = [None] * len(self.array)
        self.size = 0

    def hash(self, key):
        if key is None:
            return 0
        return hash(key) & 0x7fffffff  # Ensure non-negative

    def getIndex(self, key):
        return self.hash(key) % len(self.array)

    '''
    1. If both v1 and v2 are not None, it performs a standard equality check (v1 == v2).
    2. If v1 is None, it considers them equal only if v2 is also None. 
    This is because in a hash map context, two keys with the value None might be considered the same.
    '''
    def equals(self, v1, v2):
        return v1 == v2 if v1 is not None else v2 is None

    # def equals(self, v1, v2):
    #     if v1 is None:
    #         return v2 is None
    #     else:
    #         return v1 == v2

    def containsValue(self, value):
        if self.isEmpty():
            return False

        for node in self.array:
            while node:
                if self.equals(node.value, value):
                    return True
                node = node.next
        return False

    def containsKey(self, key):
        index = self.getIndex(key)
        node = self.array[index]
        while node:
            if self.equals(node.key, key):
                return True
            node = node.next
        return False

    def get(self, key):
        index = self.getIndex(key)
        node = self.array[index]
        while node:
            if self.equals(node.key, key):
                return node.value
            node = node.next
        return None

    def put(self, key, value):
        index = self.getIndex(key)
        node = self.array[index]
        while node:
            if self.equals(node.key, key):
                oldValue = node.value
                node.value = value
                return oldValue
            node = node.next

        new_node = Node(key, value)
        new_node.next = self.array[index]
        self.array[index] = new_node
        self.size += 1

        if self.needRehashing():
            self.rehashing()
        return None

    def needRehashing(self):
        return (self.size + 0.0) / len(self.array) >= self.load_factor

    def rehashing(self):
        oldArray = self.array
        self.array = [None] * (len(oldArray) * self.SCALE_FACTOR)
        for node in oldArray:
            while node:
                next_node = node.next
                index = self.getIndex(node.key)
                node.next = self.array[index]
                self.array[index] = node
                node = next_node
        '''        
        要rehash old list.
        拿出当前node，保存他的next。
        获得当前node的new index
        把当前node插到new index那边的第一位。
        用之前保存的next，继续rehash。
        '''

    def remove(self, key):
        index = self.getIndex(key)
        node = self.array[index]
        prev = None
        while node:
            if self.equals(node.key, key):
                if prev is None:
                    # If Head is the removed node, prev is Still null
                    self.array[index] = node.next
                else:
                    prev.next = node.next
                self.size -= 1
                return node.value
            prev = node
            node = node.next
        return None



# Example usage
if __name__ == "__main__":
    my_map = HashMap()
    my_map.put("google", 1)
    my_map.put("yahoo", 2)
    print(f"map's size: {my_map.size}")
    print(f"map is empty? {my_map.isEmpty()}")
    print(my_map.get("google"))  # Output: 1
    print(my_map.containsKey("google"))  # Output: True
    print(my_map.containsValue(15))  # Output: False
    my_map.put("Facebook", 3)
    print(f"map add key: Facebook, Value: 3")
    my_map.put("OpenAI", 4)
    print(f"map add key: OpenAI, Value: 4")
    print(f"map's size: {my_map.size}")
    my_map.remove("yahoo")
    print(f"map remove key: yahoo")
    print(f"map's size: {my_map.size}")
    print(my_map.get("yahoo"))
