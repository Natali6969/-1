class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two_lists(list1, list2):
    dummy = ListNode()
    current = dummy

    while list1 is not None and list2 is not None:
        if list1.val < list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next

        current = current.next

    if list1 is not None:
        current.next = list1
    elif list2 is not None:
        current.next = list2

    return dummy.next

# Приклад використання:
node1 = ListNode(1, ListNode(2, ListNode(4)))
node2 = ListNode(1, ListNode(3, ListNode(4)))
result = merge_two_lists(node1, node2)

# Вивід результату
while result is not None:
    print(result.val, end=" ")
    result = result.next
