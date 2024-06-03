"""

380. Insert Delete GetRandom O(1)
Medium
Topics
Companies
Implement the RandomizedSet class:

RandomizedSet() Initializes the RandomizedSet object.
bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
int getRandom() Returns a random element from the current set of elements (it's guaranteed 
that at least one element exists when this method is called). Each element must have the same probability of being returned.
You must implement the functions of the class such that each function works in average O(1) time complexity.

"""

# Hashing 
# use O(1) time complexity 
# set() operation 

import random

class RandomizedSet:

    def __init__(self):
        # set use for O(1) search operation 
        self.num_set = set()
        # list use for random select
        self.num_list = []

    def insert(self, val: int) -> bool:
        if val not in self.num_set:
            self.num_set.add(val)
            self.num_list.append(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.num_set:
            self.num_set.remove(val)
            self.num_list.remove(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        if len(self.num_set) == 0:
            return False
        else:
            random_num = random.choice(self.num_list)
            return random_num
        
if __name__ == "__main__":
    randomizedSet = RandomizedSet()
