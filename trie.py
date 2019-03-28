# @Time    : 2019/3/28 8:25
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from typing import Optional, List


class TrieNode:

    def __init__(self, val: str):
        self.val = val
        self.children: List[Optional[TrieNode]] = [None] * 26
        self.is_ending = False


class Trie:

    def __init__(self):
        self.root = TrieNode('/')

    def insert(self, val: str):
        node = self.root
        for letter in val:
            idx = ord(letter) - ord('a')
            if node.children[idx] is None:
                child = TrieNode(letter)
                node.children[idx] = child
            node = node.children[idx]
        node.is_ending = True

    def find(self, val: str) -> bool:
        node = self.root
        for letter in val:
            idx = ord(letter) - ord('a')
            if node.children[idx] is None:
                return False
            node = node.children[idx]
        return node.is_ending


if __name__ == "__main__":
    words = ['how', 'hi', 'her', 'hello', 'so', 'see']
    t = Trie()
    for w in words:
        t.insert(w)
    print(t.find('hero'))
