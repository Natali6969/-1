class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_k_sorted_lists(lists):
    import heapq

    # Міні-куча для зберігання вузлів
    min_heap = []

    # Заповнюємо кучу першим елементом кожного списку
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(min_heap, (lst.val, i, lst))

    # Голова фіктивного вузла
    dummy = ListNode()
    current = dummy

    while min_heap:
        # Витягаємо найменший елемент з кучі
        val, i, node = heapq.heappop(min_heap)
        
        # Додаємо його в результуючий список
        current.next = ListNode(val)
        current = current.next

        # Переходимо до наступного вузла в поточному списку
        if node.next:
            heapq.heappush(min_heap, (node.next.val, i, node.next))

    return dummy.next

# Приклад використання:
# Створимо три вхідні відсортовані списки
list1 = ListNode(1, ListNode(4, ListNode(5)))
list2 = ListNode(1, ListNode(3, ListNode(4)))
list3 = ListNode(2, ListNode(6))

# Помістимо їх в масив
lists = [list1, list2, list3]

# Об'єднаємо їх
result = merge_k_sorted_lists(lists)

# Виведемо результат
while result:
    print(result.val, end=" ")
    result = result.next


