"""

146. LRU Cache

Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.



Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. 
Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.


"""


# Use linked list to store key-value pairs
# get(): get value based on key is achieved using hash map 
# put(): add / update value based on input key
# update node positions requires use of linked list
# double linked list left: least recent -> right: most recent
# head pointer: least recent used
# tail pointer: most recent used
# double linked list for fast insertion and delete

class cacheNode:
    def __init__(self,key, value, prev=None, next=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        # initialise dummy nodes to avoid edge cases
        # pointer pointing to Least Recent Used and Most Recent Used
        self.LRU= cacheNode(0,0)
        self.MRU = cacheNode(0,0)
        self.LRU.next = self.MRU
        self.MRU.prev = self.LRU
        self.capacity = capacity
        self.cache = {} # for get() operation
    
    # remove a node from the linked list 
    def delete(self,node):
        prevNode = node.prev
        nextNode = node.next 
        prevNode.next = nextNode
        nextNode.prev = prevNode
        return 
    
    # add node to tail
    def insert_at_tail(self,node):
        tailNode = self.MRU.prev
        tailNode.next = node
        node.prev = tailNode
        node.next = self.MRU
        self.MRU.prev = node
        return 
    
    # find node and return node value 
    def get(self, key):
        value = -1
        if key in self.cache:
            node = self.cache[key]
            value = node.value
            # update the node to most recent used 
            # delete the node from it's current position
            self.delete(node)
            # insert node to tail
            self.insert_at_tail(node)
        return value
    
    # add node or update 
    # and delete LRU node
    def put(self, key, value):
        # if node exist, update its value
        # update the node to most recent used 
        if key in self.cache.keys():
            node = self.cache[key]
            node.value = value
            self.delete(node)
            self.insert_at_tail(node)
            return
        
        # if node does not exist, insert new node at tail
        # if reached capacity, remove LRU node
        if len(self.cache.keys()) >= self.capacity:
            node = self.LRU.next
            self.delete(node)
            del self.cache[node.key]
        
        # insert new node at tail
        newNode = cacheNode(key, value)
        self.cache[key] = newNode
        self.insert_at_tail(newNode)
        return
    
    def display(self):
        curNode = self.LRU.next
        result = []
        while curNode != self.MRU:
            result.append([curNode.key, curNode.value])
            curNode = curNode.next
        print(f"cache state: {result}")
    
    
if __name__ == "__main__":
    cache = LRUCache(2)
    test_list = [[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]
    step = 0
    for operation in test_list:
        if len(operation) == 1:
            cache.get(operation[0])
        else:
            cache.put(operation[0], operation[1])
        step += 1
        print(f"the step {step}")
        cache.display()
