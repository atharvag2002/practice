
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def has_cycle(head):
    if not head or not head.next:
        return False
    slow = head
    fast = head.next
    while slow != fast:
        if not fast or not fast.next:
            return False
        slow = slow.next
        fast = fast.next.next
    return True


def main():
    # Create list with cycle: 1 -> 2 -> 3 -> 4 -> 2 (cycle)
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2
    
    print(f"List has cycle: {has_cycle(node1)}")
    
    # List without cycle
    node5 = ListNode(5)
    node6 = ListNode(6)
    node5.next = node6
    print(f"List has cycle: {has_cycle(node5)}")


if __name__ == "__main__":
    main()
