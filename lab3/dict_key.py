# Створення словника
signals = {'green': 'go', 'yellow': 'go faster', 'red': 'smile for the camera'}

# Отримання dict_keys об'єкта
keys = signals.keys()
print(keys)  # Вивід: dict_keys(['green', 'yellow', 'red'])

# Конвертація dict_keys в список
keys_list = list(signals.keys())
print(keys_list)  # Вивід: ['green', 'yellow', 'red']
