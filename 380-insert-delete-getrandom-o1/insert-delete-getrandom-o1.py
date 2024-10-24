from random import random

class RandomizedSet:

    def __init__(self):
        self.val_idx_map = {} # { val: idx }
        self.val_arr = []

    def insert(self, val: int) -> bool:
        if val not in self.val_idx_map:
            self.val_idx_map[val] = len(self.val_arr)
            self.val_arr.append(val)

            return True
        return False
        
    def remove(self, val: int) -> bool:
        if val in self.val_idx_map:
            last_val = self.val_arr[-1]
            last_val_idx = self.val_idx_map[last_val]
            del_val_idx = self.val_idx_map[val]
            
            self.val_arr[del_val_idx] = last_val
            self.val_idx_map[last_val] = del_val_idx
            
            self.val_arr.pop()
            del self.val_idx_map[val]
            
            return True
        return False

    def getRandom(self) -> int:
        idx = floor(len(self.val_arr) * random())
        return self.val_arr[idx]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()