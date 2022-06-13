class Node():
    def __init__(self,data):
        self.data = data
        self.next = None
def middle_element(head):
    cur=head
    count = 0
    while cur:
        count+=1
        cur=cur.next
    mid = count//2
    cur = head
    for i in range(mid):
        cur = cur.next
    return cur.data



if __name__ == "__main__":

    common = Node(1)
    head1 = Node(3)
    head1.next =Node(6)
    head1.next.next =Node(9)
    head1.next.next.next = common
    head1.next.next.next.next = Node(30)
    head1.next.next.next.next.next = Node(40)

    # head2 = Node(10)
    # head2.next= common
    # head2.next.next = Node(30)
    print("middle element is",middle_element(head1))