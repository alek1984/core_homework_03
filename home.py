import random

def get_numbers_ticket(min, max, quantity):
    """
    Генерує набір унікальних випадкових чисел для лотереї.

    Параметри:
    min (int): Мінімальне можливе число у наборі (не менше 1).
    max (int): Максимальне можливе число у наборі (не більше 1000).
    quantity (int): Кількість чисел, які потрібно вибрати.

    Повертає:
    list: Відсортований список унікальних випадкових чисел.
          Якщо параметри некоректні, повертає порожній список.
    """
    # Перевірка коректності вхідних параметрів
    if min < 1 or max > 1000 or quantity > (max - min + 1) or quantity < 1:
        return []
    
    # Генерація унікальних випадкових чисел
    numbers = random.sample(range(min, max + 1), quantity)
    return sorted(numbers)

# Приклади використання
print(get_numbers_ticket(1, 49, 6))  # Наприклад, [5, 12, 23, 34, 42, 48]
print(get_numbers_ticket(1, 36, 5))  # Наприклад, [3, 14, 18, 22, 35]
print(get_numbers_ticket(10, 20, 15))  # Некоректно: повертає []
print(get_numbers_ticket(1, 1000, 10))  # Список із 10 чисел між 1 і 1000
