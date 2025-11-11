class RandomizedSet:

    def __init__(self):
        # initialize list
        self.store = []
        # initialize hashmap for indices
        self.track = {}

    def insert(self, val: int) -> bool:
        # check if val is present
        if val in self.track:
            return False

        # append to store
        self.store.append(val)
        # store index
        self.track[val] = len(self.store) - 1

        return True

    def remove(self, val: int) -> bool:
        # check if val doesnt exist
        if val not in self.track:
            return False
        
        lastelement = self.store[-1]
        valindex = self.track[val]
        lastelementidx = self.track[lastelement]

        # interchange the values in store
        self.store[valindex], self.store[lastelementidx] = self.store[lastelementidx], self.store[valindex]
        
        # interchange the indices
        self.track[val], self.track[lastelement] = self.track[lastelement], self.track[val]
        
        # remove val
        self.track.pop(val)
        self.store.pop()

        return True

    def getRandom(self) -> int:
        return random.choice(self.store)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()