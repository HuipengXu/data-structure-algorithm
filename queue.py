from single_linked_list import Node

class SingleLinkedQueue:

    def __init__(self):
        self._head = None
        self._tail = None
        self.length = 0

    def enqueue(self, item):
        new_item = Node(item)
        if not self._head:
            self._head = new_item
        else:
            self._tail._next = new_item
        self._tail = new_item
        self.length += 1
        return True

    def dequeue(self):
        if not self._head:
            return None
        val = self._head.val
        self._head = self._head._next
        self.length -= 1
        return val

    def __len__(self):
        return self.length

    def __repr__(self):
        return "<SingleLinkedQueue: %d>" % self.length

class ArrayQueue:

    def __init__(self, capacity=10):
        self._items = []
        self._head = 0
        self._tail = 0
        self.capacity = capacity

    def enqueue(self, item):
        if self._tail == self.capacity:
            if self._head == 0:
                return False
            self._items[0: self._tail - self._head] = self._items[self._head: self._tail]
            self._tail -= self._head
            self._head = 0
        if self.capacity > len(self._items):
            self._items.append(item)
        else:
            self._items[self._tail] = item
        self._tail += 1
        return True

    def dequeue(self):
        if self._head == self._tail:
            return None
        ret = self._items[self._head]
        self._head += 1
        return ret


    def __len__(self):
        return len(self._items)

    def __repr__(self):
        return "<ArrayQueue: [%s]>" % ', '.join(str(item) for item in self._items)

class CircleArrayQueue:

    def __init__(self, capacity):
        self._items = []
        self._head = 0
        self._tail = 0
        self.capacity = capacity

    def enqueue(self, item):
        if (self._tail + 1) % self.capacity == self._head:
            return False
        if self.capacity > len(self._items):
            self._items.append(item)
        else:
            self._tail %= self.capacity
            self._items[self._tail] = item
        self._tail += 1
        return True

    def dequeue(self):
        if self._head == self._tail:
            return None
        ret = self._items[self._head]
        self._head = (self._head + 1) % self.capacity
        return ret

    def __len__(self):
        return len(self._items)

    def __repr__(self):
        return "<CircleArrayQueue: [%s]>" % ', '.join(str(item) for item in self._items)

class ListQueue:

    def __init__(self, capacity=10):
        self._items = []
        self.capacity = capacity

    def enqueue(self, item):
        if len(self._items) == self.capacity:
            return False
        self._items.append(item)
        return True

    def dequeue(self):
        if len(self._items) == 0:
            return None
        return self._items.pop(0)

    def __len__(self):
        return len(self._items)

    def __repr__(self):
        return "<ListQueue: [%s]>" % ', '.join(str(item) for item in self._items)
            

if __name__ == "__main__":
    q = ListQueue()
    for i in range(5):
        state = q.enqueue(i)
        print(state)
    # for _ in range(10):
    #     print(q.dequeue())
    # q.enqueue(90)
    # q.enqueue(100)
    print(q.dequeue())
    q.enqueue(20)
    print(q.dequeue())
    q.enqueue(30)
    print(q.dequeue())
    q.enqueue(40)
    print(q)
    
        
