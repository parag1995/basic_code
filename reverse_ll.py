class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

def reverse_linkedlist(head1):
    cur = head1
    pre = None
    if head1 is None:
        return
    cur = head1
    pre = None
    while cur:
        nxt = cur.next
        cur.next = pre
        pre = cur
        cur = nxt
    return pre

def traverse_ll(ptr):
    while ptr:
        print(ptr.data)
        ptr = ptr.next


if __name__ == "__main__":

    common = Node(1)
    head1 = Node(3)
    head1.next =Node(6)
    head1.next.next =Node(9)
    head1.next.next.next = common
    head1.next.next.next.next = Node(30)
    head1.next.next.next.next.next = Node(40)

    ptr = reverse_linkedlist(head1)
    traverse_ll(ptr)