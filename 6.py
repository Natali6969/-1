class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def double_linked_list(head):
    carry = 0
    dummy = ListNode(0)
    current = dummy
    
    while head is not None or carry > 0:
        x = head.val if head is not None else 0
        total = x * 2 + carry
        current.next = ListNode(total % 10)
        carry = total // 10

        if head is not None:
            head = head.next
        current = current.next
    
    if carry > 0:
        current.next = ListNode(carry)

    return dummy.next

# Приклад використання:
# Створимо вхідний список: 9 -> 9 -> 9
head = ListNode(9, ListNode(9, ListNode(9)))

# Викликаємо функцію для подвоєння числа
result_head = double_linked_list(head)

# Виведемо результат
while result_head is not None:
    print(result_head.val, end=" ")
    result_head = result_head.next


