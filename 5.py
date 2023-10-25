class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def delete_node(node):
    if node is None or node.next is None:
        return

    # Копіюємо значення наступного вузла в поточний вузол
    node.val = node.next.val

    # Видаляємо наступний вузол
    node.next = node.next.next

# Приклад використання:
# Створимо вхідний список: 4 -> 5 -> 1 -> 9
head = ListNode(4, ListNode(5, ListNode(1, ListNode(9))))

# Задамо вузол, який потрібно видалити (наприклад, вузол зі значенням 5)
node_to_delete = head.next

# Викликаємо функцію для видалення вузла
delete_node(node_to_delete)

# Виведемо результат
while head is not None:
    print(head.val, end=" ")
    head = head.next



