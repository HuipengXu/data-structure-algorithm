# 节点类
class Node:
    
    def __init__(self, val=None, _next=None):
        self.val = val
        self._next = _next
        
    def __repr__(self):
        return "<Node: %s>" % str(self.val)

# 单链表
class SingleLinkedList:

    def __init__(self, head=None):
        self.head = Node(head)
        self.length = 0

    def is_empty(self):
        return True if not self.length else False

    def append(self, val_or_node):
        if isinstance(val_or_node, Node):
            new_node = val_or_node
        else:
            new_node = Node(val_or_node)

        if self.head.val is None:
            self.head = new_node
        else:
            node = self.head
            while node._next:
                node = node._next
            node._next = new_node
        self.length += 1
        return 

    def update(self, index, val):
        if self.length <= index or index < 0:
            print('out of index')
            return 
        node = self.head
        for _ in range(index):
            node = node._next
        node.val = val
        return 

    def pop(self, index=0):
        if self.length <= index or index < 0:
            print("out of index")
            return None

        if index == 0:
            current_node_val = self.head.val
            self.head = self.head._next
        else:
            node = self.head
            for _ in range(index-1):
                node = node._next
            prev = node
            current_node_val = prev._next.val
            after = node._next._next
            prev._next = after
        self.length -= 1
        return current_node_val

    def insert(self, index, val_or_node):
        if isinstance(val_or_node, Node):
            new_node = val_or_node
        else:
            new_node = Node(val_or_node)

        node = self.head
        if index > self.length:
            while node._next:
                node = node._next
            node._next = new_node
        elif index <= 0:
            new_node._next = self.head
            self.head = new_node
        else:
            for _ in range(index-1):
                node = node._next
            prev = node
            current = node._next
            prev._next = new_node
            new_node._next = current
        self.length += 1
        return 

    def clear(self):
        self.head = None
        self.length = 0
        return 

    def get_item(self, index):
        if index >= self.length or index < 0:
            print("out of index")
            return 
        
        node = self.head
        for _ in range(index):
            node = node._next
        
        return node.val

    def get_index(self, val):
        node = self.head
        for i in range(self.length):
            if node.val == val:
                return i
            node = node._next
        return None

    def print_all(self):
        node = self.head
        if not node:
            print('None')
            return 
        while node._next:
            print(node.val)
            node = node._next
        print(node.val)
        return  

    def __repr__(self):
        return "<SingleLinkedList: %s>" % str(self.head.val)

    def __len__(self):
        return self.length

    def __getitem__(self, index):
        return self.get_item(index)

    def __setitem__(self, index, val):
        return self.update(index, val)


if __name__ == "__main__":
    sll = SingleLinkedList()
    for i in range(10):
        sll.append(i)
    print(sll.pop())
    # print(sll.get_index(14))
    # print('---------------length---------------')
    # print(len(sll))
    # print('---------------all_val---------------')
    # sll.print_all()

    
    