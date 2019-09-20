"""
LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
"""
class LinkedNode(object):
    def __init__(self, key = None, value = None, prev = None, next = None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next

class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.LRU_cache = {}
        self.capacity = capacity
        self.dummy = LinkedNode()
        self.tail = LinkedNode()
    
    def del_head(self):
        head = self.dummy.next
        print(head.key, head.value)
        self.dummy.next = head.next
        self.LRU_cache.pop(head.key)

    def extract_node(self, key):
        node = self.LRU_cache[key]
        # change prev -> node -> next // prev -> next
        if node.prev != None:
            node.prev.next = node.next
            node.next.prev = node.prev
        if self.dummy.next == node:
            self.dummy.next = node.next
            node.next.prev = None

    def attach_tail(self, key):
        node = self.LRU_cache[key]
        
        if self.tail.next != None:
            self.tail.next.next = node
            node.prev = self.tail.next
        
        self.tail.next = node
        node.next = None        
        
    # change "prev->node->next...->tail"
    # to "prev->next->...->tail->node"
    def move_to_tail(self, key):
        if self.tail.next == self.LRU_cache[key]:
            return
        self.extract_node(key)
        self.attach_tail(key)

    def append(self, node):
        if self.dummy.next is None:
            self.dummy.next = node
        
        if len(self.LRU_cache) == self.capacity:
            self.del_head()
        
        self.LRU_cache[node.key] = node
        self.attach_tail(node.key)

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.LRU_cache:
            self.move_to_tail(key)
            return self.LRU_cache[key].value
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.LRU_cache:
            self.move_to_tail(key)
            self.LRU_cache[key].value = value
        else:
            self.append(LinkedNode(key, value))
