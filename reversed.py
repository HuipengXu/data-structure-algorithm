from single_linked_list import SingleLinkedList

def reverse_single_linked(single_linked):
    prev = None
    node = single_linked.head
    while node:
        after = node._next
        node._next = prev
        prev = node
        node = after
    single_linked.head = prev
    return single_linked

if __name__ == "__main__":
    test = SingleLinkedList()
    # for i in range(10):
    #     test.append(i)
    test = reverse_single_linked(test)
    test.print_all()
