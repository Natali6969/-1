class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_k_group(head, k):
    def reverse_list(node):
        prev = None
        while node:
            next_node = node.next
            node.next = prev
            prev = node
            node = next_node
        return prev

    def get_list_length(node):
        length = 0
        while node:
            length += 1
            node = node.next
        return length

    length = get_list_length(head)
    dummy = ListNode(0)
    dummy.next = head
    prev_group_end = dummy

    while length >= k:
        group_start = prev_group_end.next
        group_end = group_start
        for _ in range(k - 1):
            group_end = group_end.next

        next_group_start = group_end.next
        group_end.next = None

        prev_group_end.next = reverse_list(group_start)
        group_start.next = next_group_start

        prev_group_end = group_start
        length -= k

    return dummy.next

# Приклад використання:
# Створимо вхідний відсортований список
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

# Помістимо його в змінну k
k = 2

# Перевернемо вузли в групах по k
result = reverse_k_group(head, k)

# Виведемо результат
while result:
    print(result.val, end=" ")
    result = result.next



