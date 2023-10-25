class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reorder_list(head):
    if head is None or head.next is None:
        return head

    # Знайдемо середину списку
    slow, fast = head, head
    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next

    # Розбиваємо список на дві частини
    second_half = slow.next
    slow.next = None

    # Реверсуємо другу половину
    prev, current = None, second_half
    while current is not None:
        temp = current.next
        current.next = prev
        prev = current
        current = temp

    # Об'єднуємо дві частини списку
    first, second = head, prev
    while second is not None:
        temp1, temp2 = first.next, second.next
        first.next, second.next = second, temp1
        first, second = temp1, temp2

    return head

# Приклад використання:
# Створимо вхідний список: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

# Викликаємо функцію для перевпорядкування
reorder_list(head)

# Виведемо результат
while head is not None:
    print(head.val, end=" ")
    head = head.next


