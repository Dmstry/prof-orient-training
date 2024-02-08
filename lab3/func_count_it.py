def count_it(sequence):
    # Перетворення рядка в список чисел
    num_list = [int(num) for num in sequence]
    # Створення словника для підрахунку кожного числа
    num_count = {num: num_list.count(num) for num in set(num_list)}
    # Сортування словника за кількістю повторень та вибірка 3 найбільших
    sorted_num_count = dict(sorted(num_count.items(), key=lambda item: item[1], reverse=True)[:3])
    return sorted_num_count

# Приклад виклику функції
sequence = "11111555999999966742"
print(count_it(sequence))
