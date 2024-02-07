s = "Hello World"
# Перетворення рядка у нижній регістр
lower_s = s.lower()

# Розділення на слова та сортування символів кожного слова
sorted_words = [''.join(sorted(word)) for word in lower_s.split()]

# З'єднання відсортованих слів назад у рядок із збереженням пробілів
result = ' '.join(sorted_words)

print(result)

