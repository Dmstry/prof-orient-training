words = []
print("Введіть слова (порожній рядок для завершення):")

while True:
    word = input()
    if word == "":
        break
    if word not in words:
        words.append(word)

print("Унікальні слова у порядку введення:")
for word in words:
    print(word)
