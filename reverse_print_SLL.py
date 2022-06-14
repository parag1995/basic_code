class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

def reverse_linkedlist(head1):
    if head1 is None:
        return
    reverse_linkedlist(head1.next)
    print(head1.data)


if __name__ == "__main__":

    common = Node(1)
    head1 = Node(3)
    head1.next =Node(6)
    head1.next.next =Node(9)
    head1.next.next.next = common
    head1.next.next.next.next = Node(30)
    head1.next.next.next.next.next = Node(40)

    reverse_linkedlist(head1)