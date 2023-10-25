class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def partition(head, x):
    # Створимо два вказівника для двох розділених списків
    before_head = ListNode(0)
    before = before_head
    after_head = ListNode(0)
    after = after_head

    while head:
        # Розділити вузли за значенням x
        if head.val < x:
            before.next = head
            before = before.next
        else:
            after.next = head
            after = after.next

        head = head.next

    # З'єднаємо дві частини
    before.next = after_head.next
    after.next = None

    return before_head.next

# Приклад використання:
# Створимо вхідний відсортований список
head = ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(5, ListNode(2))))))

# Значення для розділення
x = 3

# Викликаємо функцію розділення
result = partition(head, x)

# Виведемо результат
while result:
    print(result.val, end=" ")
    result = result.next


