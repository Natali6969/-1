class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def has_cycle(head):
    # Перевіряємо, чи є порожній список або тільки один вузол
    if head is None or head.next is None:
        return False

    # Встановлюємо повільний та швидкий вказівники
    slow = head
    fast = head.next

    while slow != fast:
        # Якщо швидкий вказівник дійшов до кінця списку (немає циклу)
        if fast is None or fast.next is None:
            return False

        # Пересуваємо повільний вказівник на один вузол
        slow = slow.next

        # Пересуваємо швидкий вказівник на два вузли
        fast = fast.next.next

    # Якщо цикл виявлений
    return True

# Приклад використання:
# Створимо циклічний список: 1 -> 2 -> 3 -> 4 -> 2
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = head.next  # Створюємо цикл

# Перевіряємо, чи є цикл
result = has_cycle(head)

# Виведемо результат
print(result)
