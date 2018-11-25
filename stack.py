from single_linked_list import SingleLinkedList, Node

# 基于 list 实现固定容量的栈
class ListStack:

    def __init__(self, capacity):
        self.val = []
        self.capacity = capacity

    # 入栈
    def push(self, data):
        if len(self.val) >= self.capacity:
            return False
        self.val.append(data)
        return True

    # 出栈
    def pop(self):
        if len(self.val) == 0:
            return None
        return self.val.pop()

    def __len__(self):
        return len(self.val)

    def __repr__(self):
        """
        显示栈的固定容量
        """
        return "<ListStack: %d>" % self.capacity

# 基于 list 实现动态扩容的栈
class DynamicListStack:

    def __init__(self):
        self.val = []

    def push(self, data):
        self.val.append(data)
        return True

    def pop(self):
        if len(self.val) == 0:
            return None
        return self.val.pop()

    def __len__(self):
        return len(self.val)

    def __repr__(self):
        """
        显示栈的当前大小
        """
        return "<DynamicListStack: %d>" % len(self.val)

# 直接调用已经写好的接口
class SingleLinkedStack0:

    def __init__(self):
        self.items = SingleLinkedList()
        self.length = 0

    def push(self, item):
        self.items.append(item)
        self.length += 1
        return True

    def pop(self):
        if len(self.items) == 0:
            return None
        return self.items.pop(self.length - 1)

    def __len__(self):
        return len(self.items)

    def __repr__(self):
        """
        显示栈的容量
        """
        return "<SingleLinkedStack0: %d>" % self.length

# 未调用现成的接口，并从链表的尾部插入
class SingleLinkedStack1:
    def __init__(self, head=None):
        self.head = head
        self.length = 0

    def push(self, item):
        node = self.head
        new_node = Node(item)
        if not node:
            self.head = new_node
            self.length += 1
            return True
        while node:
            prev = node
            node = node._next
        prev._next = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        node = self.head
        if not node._next:
            self.head = None
            self.length -= 1
            return node.val
        while node:
            prev = node
            node = node._next
            if not node._next:
                break
        prev._next = None
        self.length -= 1
        return node.val

    def __len__(self):
        return self.length

    def __repr__(self):
        """
        显示栈的大小
        """
        return "<SingleLinkedStack1: %d>" % self.length

# 未调用现成的接口，并从链表的头部插入      
class SingleLinkedStack2:

    def __init__(self, head=None):
        self.head = head
        self.length = 0

    def push(self, item):
        new_node = Node(item)
        new_node._next = self.head
        self.head = new_node
        self.length += 1
        return True

    def pop(self):
        if not self.head:
            return None
        pop_value = self.head.val
        self.head = self.head._next
        return pop_value

    def __len__(self):
        return self.length

    def __repr__(self):
        """
        显示栈的大小
        """
        return "<SingleLinkedStack2: %d>" % self.length

        


if __name__ == "__main__":
    s = SingleLinkedStack2()
    for i in range(10):
        s.push(i)
    print(s.push(12))
    print(s.pop())
    print(s.pop())
    print(s)