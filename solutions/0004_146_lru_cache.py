# Solution for LeetCode 146: LRU Cache
class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        """
        Initialize LRU Cache with given capacity.
        
        Time Complexity: O(1) for both get and put operations
        Space Complexity: O(capacity) - we store at most capacity items
        
        Args:
            capacity: Maximum number of items the cache can hold
        """
        self.capacity = capacity
        self.cache = {}  # Dictionary to store key -> node mapping
        
        # Create dummy head and tail nodes for the doubly linked list
        self.head = Node()  # Dummy head
        self.tail = Node()  # Dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node):
        """Remove node from the linked list."""
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add_to_head(self, node: Node):
        """Add node right after head (most recently used position)."""
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        """
        Get the value of the key if it exists in the cache, otherwise return -1.
        
        Args:
            key: Key to look up
            
        Returns:
            Value associated with key, or -1 if not found
        """
        if key in self.cache:
            node = self.cache[key]
            # Move accessed node to head (most recently used)
            self._remove(node)
            self._add_to_head(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        """
        Insert or update the value of the key.
        If the cache reaches capacity, evict the least recently used item.
        
        Args:
            key: Key to insert or update
            value: Value to associate with the key
        """
        if key in self.cache:
            # Update existing key
            node = self.cache[key]
            node.value = value
            # Move to head (most recently used)
            self._remove(node)
            self._add_to_head(node)
        else:
            # Insert new key
            if len(self.cache) >= self.capacity:
                # Remove least recently used item (before tail)
                lru_node = self.tail.prev
                self._remove(lru_node)
                del self.cache[lru_node.key]
            
            # Add new node
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add_to_head(new_node)

# Test the solution
if __name__ == "__main__":
    # Test case from LeetCode example
    cache = LRUCache(2)
    
    cache.put(1, 1)
    cache.put(2, 2)
    print(cache.get(1))  # returns 1
    cache.put(3, 3)      # evicts key 2
    print(cache.get(2))  # returns -1 (not found)
    cache.put(4, 4)      # evicts key 1
    print(cache.get(1))  # returns -1 (not found)
    print(cache.get(3))  # returns 3
    print(cache.get(4))  # returns 4