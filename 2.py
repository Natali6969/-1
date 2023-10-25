class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def delete_duplicates(head):
    current = head

    while current is not None and current.next is not None:
        if current.val == current.next.val:
            # Видаляємо дублікат, змінюючи вказівник
            current.next = current.next.next
        else:
            # Переходимо до наступного вузла
            current = current.next

    return head

# Приклад використання:
# Створимо вхідний відсортований список: 1 -> 1 -> 2
head = ListNode(1, ListNode(1, ListNode(2)))
result = delete_duplicates(head)

# Виведемо результат
while result is not None:
    print(result.val, end=" ")
    result = result.next

