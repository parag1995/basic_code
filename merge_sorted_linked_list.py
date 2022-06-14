class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

def merge_sorted_ll(head1,head2):
    dummy = Node(None)
    spare = dummy
    while head1 and head2:
        if head1.data < head2.data:
            spare.next = head1
            head1 = head1.next
        else:
            spare.next = head2
            head2 = head2.next
        spare = spare.next

    if head1:
        spare.next = head1
    elif head2:
        spare.next = head2

    return dummy.next

def traverse_ll(ptr):
    while ptr:
        print(ptr.data)
        ptr = ptr.next



if __name__ == "__main__":

    # common = Node(1)
    head1 = Node(1)
    head1.next =Node(3)
    head1.next.next =Node(7)
    # head1.next.next.next = common
    # head1.next.next.next.next = Node(30)

    head2 = Node(1)
    # head2.next= common
    head2.next = Node(2)
    ptr = merge_sorted_ll(head1,head2)
    traverse_ll(ptr)