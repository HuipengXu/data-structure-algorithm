from single_linked_list import SingleLinkedList, Node

def least_recently_used(data, cache, n=10):
    if data == None:
        return cache

    prev = None
    node = cache.head
    while node:
        if node.val == data:
            if not prev:
                return cache
            prev._next = node._next
            node._next = cache.head
            cache.head = node
            return cache
        # 确保能拿到倒数第二个方便后面缓存满的时候删掉最后一个
        if node._next:
            prev = node
        node = node._next
    # 如果不在缓存中
    # 如果缓存已满，删掉最后一个
    if cache.length == n:
        prev._next = None
        cache.length -= 1
    # 缓存未满
    new_node = Node(data)
    new_node._next = cache.head
    cache.head = new_node
    cache.length += 1
    return cache

if __name__ == "__main__":
    test = SingleLinkedList()
    for i in range(10):
        test.append(i)
    test = least_recently_used(20, test, 10)
    test.print_all()
    print('-----------length-----------')
    print(test.length)
    print('--------------test---------------')
    test = least_recently_used(21, test, 10)
    test.print_all()