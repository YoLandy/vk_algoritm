# в шаде короче была задачка которая как то относится к теме префиксные суммы

"""
условие:

кто то там, какие то кринжкоины покупал и решил что вот давайте брать окно из k элементов в курсе валют и складывать минимальное и максимальное значение в окне. И надо выписать макисмум этого



Короооче, я был приятно удивлен что есть линейное решение.
Сначала я пытался делать с помощью бинарного дерева поиска (типа дерево из K элементов окна, каждый раз добавляю новый и убираю старый, ну все за logK короче), но оно падало на каких то тестах
В итоге прошло такое решение
"""


from collections import deque

n, k = map(int, input().split())
nums = list(map(int, input().split()))

max_sum = -float("inf")
min_deque = deque()
max_deque = deque()

for i in range(n):
    # Удаляем элементы, выходящие из левой границы окна
    while min_deque and min_deque[0] < i - k + 1:
        min_deque.popleft()
    while max_deque and max_deque[0] < i - k + 1:
        max_deque.popleft()

    # Обновляем deque для минимумов (поддерживаем неубывающий порядок)
    while min_deque and nums[i] <= nums[min_deque[-1]]:
        min_deque.pop()
    min_deque.append(i)

    # Обновляем deque для максимумов (поддерживаем невозрастающий порядок)
    while max_deque and nums[i] >= nums[max_deque[-1]]:
        max_deque.pop()
    max_deque.append(i)

    # Формируем сумму только для полноценных окон
    if i >= k - 1:
        current_sum = nums[min_deque[0]] + nums[max_deque[0]]
        max_sum = max(max_sum, current_sum)

print(max_sum)
