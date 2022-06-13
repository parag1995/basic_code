class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

def getIntersectionNode(head1, head2):

    c1 = getCount(head1)
    c2 = getCount(head2)

    if c1>c2:
        d = c1-c2
        return _getIntersectionNode(d,head1,head2)
    else:
        d = c2-c1
        return _getIntersectionNode(d,head2,head1)

def _getIntersectionNode(d,head1,head2):
    current1=head1
    current2 = head2

    for i in range(d):
        if current1 is None:
            return -1
        current1=current1.next
    while current1 is not None and current2 is not None:
        if current1 is current2:
            return current1.data
        current1=current1.next
        current2=current2.next
    return -1

def getCount(node):
    counter = 0
    cur = node
    while cur is not None:
        counter+=1
        cur = cur.next
    return counter










if __name__ == "__main__":

    common = Node(15)
    head1 = Node(3)
    head1.next =Node(6)
    head1.next.next =Node(9)
    head1.next.next.next = common
    head1.next.next.next.next = Node(30)

    head2 = Node(10)
    head2.next= common
    head2.next.next = Node(30)
    print("The node of intersection is ",getIntersectionNode(head1,head2))

