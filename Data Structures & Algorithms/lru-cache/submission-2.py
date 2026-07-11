class Node:
    def __init__(self, key, value, left, right):
        self.key = key
        self.value = value
        self.left = left
        self.right = right

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.dummy_right = Node(None, None, None, None)
        self.dummy_left = Node(None, None, None, self.dummy_right)
        self.dummy_right.left = self.dummy_left

    def remove(self, node):
        prev = node.left
        nxt = node.right
        prev.right = nxt
        nxt.left = prev

    def insert(self, node):
        node.right = self.dummy_left.right
        node.left = self.dummy_left
        self.dummy_left.right.left = node
        self.dummy_left.right = node

    def get(self, key: int) -> int:
        if key in self.cache:
            temp = self.cache[key]
            self.remove(temp)
            self.insert(temp)
            return temp.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value, None, None)
        self.insert(self.cache[key])
        if len(self.cache) > self.capacity:
            rem = self.dummy_right.left
            del self.cache[rem.key]
            self.remove(rem)

        
