from single_linked_list import SingleLinkedList

def is_palindrome1(single_linked):
    # 如果回文串长度为 0 或 1 则为回文串
    if single_linked.length in [0, 1]:
        return True
    fast, slow = single_linked.head, single_linked.head
    # 寻找中间节点
    while fast._next and fast._next._next:
        slow = slow._next
        fast = fast._next._next
    # 后半部分逆序
    prev = slow._next
    if not prev._next:
        second_part = SingleLinkedList(prev)
    else:
        current = prev._next
        after = prev._next._next
        prev._next = None
        while True:
            current._next = prev
            prev = current
            current = after
            if not current:
                second_part = SingleLinkedList(prev)
                break
            else:
                after = current._next
    # 判断是否是回文串
    node1 = single_linked.head
    node2 = second_part.head
    while node2:
        if node1.val != node2.val:
            return False
        else:
            node1 = node1._next
            node2 = node2._next
    return True

# 简洁版本
def is_palindrome2(single_linked):
    if single_linked.length in [0, 1]:
        return True

    prev = None
    fast = single_linked.head
    slow = single_linked.head

    # 慢指针前进过程中前半部分逆序
    while fast and fast._next:
        fast = fast._next._next
        next_ = slow._next
        slow._next = prev
        prev = slow
        slow = next_

    # 针对奇数情况
    if fast:
        slow = slow._next

    # 对比
    while slow:
        if slow.val != prev.val:
            return False
        else:
            slow = slow._next
            prev = prev._next
    return True
    
    

if __name__ == "__main__":
    test = SingleLinkedList()
    for i in ['a', 'b']:
        test.append(i)

    print(is_palindrome2(test))