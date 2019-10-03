# '''
# Linked List hash table key/value pair
# '''


class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''

    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity
        self.count = 0
        # self._size = size
        # self._hashit = hashit

    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        # return self._hashit(key) % self._size
        return hash(key)

    def _hash_djb2(self, key):

        # return self._hashit(key) % self._size
        '''
        Hash an arbitrary key using DJB2 hash
        
        OPTIONAL STRETCH: Research and implement DJB2
        '''
        # pass

    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity

    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        if self.count >= self.capacity:
            self.resize()

        i = self._hash_mod(key)  # i is recognized as index
        node = self.storage[i]
        pair = LinkedPair(key, value)

        while node is not None and self.storage[i].key is not key:
            next_ = node
            node = next_.next

        if node is not None:
            node.value = value
        else:
            pair.next = self.storage[i]
            self.storage[i] = pair

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        node = self.storage[index]
        next_node = None
        while node is not None and node.key != key:
            next_node = node
            node = next_node.next
        if node is None:
            print("Can't find key")
        else:
            if next_node is None:
                self.storage[index] = node.next
            else:
                next_node.next = node.next

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        node = self.storage[index]

        while node is not None:
            if node.key == key:
                return node.value
            node = node.next

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        old_storage = self.storage
        self.capacity *= 2
        self.storage = [None] * self.capacity
        pair = None
        for i in old_storage:
            pair = i
            while pair is not None:
                self.insert(pair.key, pair.value)
                pair = pair.next


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
