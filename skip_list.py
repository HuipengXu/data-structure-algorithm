# @Time    : 2018/12/10 20:41
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

# 跳表的一种实现方法。
# 跳表中存储的是正整数，并且存储的是不重复的。

from random import randint
from typing import Optional

# 节点类
class Node:

    def __init__(self, val: Optional[int]=None):
        self.val = val
        self.forwards = None
        self.max_level = 0

    def __repr__(self):
        return "<Node: %d>" % self.val

class SkipList:

    def __init__(self):
        self.head = Node()
        self._max_level = 16
        self.head.forwards = [None] * self._max_level
        self._level_count = 1

    def find(self, val: int) -> Optional[Node]:
        p = self.head
        for i in range(self._level_count-1, -1, -1):
            while p.forwards[i] and p.forwards[i].val < val:
                p = p.forwards[i]
        if p.forwards[0] != None and p.forwards[0].val == val:
            return p.forwards[0]
        else:
            return None

    def insert(self, val: int):
        # TODO 随机数的选取存在问题
        level = randint(1, self._max_level)
        new_node = Node(val)
        new_node.forwards = [None] * level
        new_node.max_level = level
        update = [self.head] * level
        p = self.head
        for i in range(level-1, -1, -1):
            while p.forwards[i] and p.forwards[i].val < val:
                p = p.forwards[i]
            update[i] = p
        for i in range(level):
            new_node.forwards[i] = update[i].forwards[i]
            update[i].forwards[i] = new_node
        if self._level_count < level: self._level_count = level

    def delete(self, val: int):
        update = [None] * self._level_count
        p = self.head
        for i in range(self._level_count-1, -1, -1):
            while p.forwards[i] and p.forwards[i].val < val:
                p = p.forwards[i]
            update[i] = p
        if p.forwards[0] and p.forwards[0].val == val:
            for i in range(self._level_count-1, -1, -1):
                if update[i].forwards[i] != None and update[i].forwards[i].val == val:
                    update[i].forwards[i] = update[i].forwards[i].forwards[i]

    def print_all(self):
        p = self.head
        while p.forwards[0]:
            p = p.forwards[0]
            print(p.val)


if __name__ == "__main__":
    sl = SkipList()
    for i in range(13):
        sl.insert(i)
    sl.print_all()
    print(sl.find(12))
    print('---------------------')
    for i in range(13, 6, -1):
        sl.delete(i)
    sl.print_all()
    print('---------------------')

